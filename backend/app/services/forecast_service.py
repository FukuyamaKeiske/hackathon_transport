import httpx
from typing import List, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.forecasts import Forecast
from app.core.config import settings
from datetime import datetime

async def generate_forecasts(waypoints: List[Tuple[float, float]], mode: str, departure_time: int):
    # Яндекс Карт
    yandex_url = "https://api.routing.yandex.net/v2/route"
    yandex_params = {
        "apikey": settings.YANDEX_MAPS_API_KEY,
        "waypoints": "|".join(f"{lat},{lon}" for lat, lon in waypoints),
        "mode": mode,
        "departure_time": departure_time or int(datetime.now().timestamp()),
        "traffic": "realtime"  # Учитываем пробки
    }
    
    async with httpx.AsyncClient() as client:
        yandex_response = await client.get(yandex_url, params=yandex_params)
        yandex_data = yandex_response.json()

    # 2ГИС
    twogis_url = "http://routing.api.2gis.com/routing/7.0.0/global"
    twogis_payload = {
        "points": [{"lon": lon, "lat": lat, "type": "stop"} for lat, lon in waypoints],
        "transport": mode,
        "route_mode": "fastest",
        "traffic_mode": "jam",
        "output": "detailed"
    }

    async with httpx.AsyncClient() as client:
        twogis_response = await client.post(twogis_url, json=twogis_payload)
        twogis_data = twogis_response.json()

    # Обработка данных и сохранение в БД
    forecast_list = []
    
    # Обработка данных от Яндекс Карт
    if yandex_data.get("route"):
        for leg in yandex_data["route"]["legs"]:
            forecast = Forecast(
                timestamp=datetime.utcnow(),
                location=f"POINT({waypoints[0][1]} {waypoints[0][0]})",
                predicted_density=calculate_density(leg),  # Логика для плотности
                predicted_speed=calculate_speed(leg)  # Логика для скорости
            )
            forecast_list.append(forecast)

    # Обработка данных от 2ГИС
    if "result" in twogis_data:
        for route in twogis_data["result"]:
            forecast = Forecast(
                timestamp=datetime.utcnow(),
                location=f"POINT({route['query']['points'][0]['lat']} {route['query']['points'][0]['lon']})",
                predicted_density=calculate_density(route),  # Логика для плотности
                predicted_speed=calculate_speed(route)  # Логика для скорости
            )
            forecast_list.append(forecast)

    # Сохранение в БД
    if forecast_list:
        async with AsyncSession() as session:
            session.add_all(forecast_list)
            await session.commit()

    return forecast_list

def calculate_density(leg):
    # Логика для расчета плотности
    total_distance = leg.get("total_distance", 0)  # Дистанция в метрах
    total_duration = leg.get("total_duration", 1)  # Время в секундах (не может быть 0)

    # Пример: плотность = количество автомобилей на 1 км
    density = (total_distance / 1000) / (total_duration / 60)  # Автомобили на км/мин
    return max(0, density)  # Не может быть отрицательной плотности

def calculate_speed(leg):
    # Логика для расчета скорости
    total_distance = leg.get("total_distance", 0)  # Дистанция в метрах
    total_duration = leg.get("total_duration", 1)  # Время в секундах (не может быть 0)

    # Скорость в км/ч
    speed = (total_distance / 1000) / (total_duration / 3600)  # км/ч
    return max(0, speed)  # Не может быть отрицательной скорости
