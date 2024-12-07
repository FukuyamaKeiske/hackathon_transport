from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.environmental_data import EnvironmentalData
from datetime import datetime

async def get_environmental_data(db: AsyncSession):
    result = await db.execute(EnvironmentalData.__table__.select())
    return result.scalars().all()

async def add_environmental_data(db: AsyncSession, data: dict):
    # Расчет выбросов на основе расстояния
    distance_m = data['distance']  # Предположим, что расстояние передаётся в метрах
    emission_level = calculate_emission(distance_m)

    new_data = EnvironmentalData(
        timestamp=datetime.fromisoformat(data['timestamp']),
        location=f"POINT({data['longitude']} {data['latitude']})",
        emission_level=emission_level
    )
    db.add(new_data)
    await db.commit()
    return new_data

def calculate_emission(distance_m: float) -> float:
    # Конвертация расстояния в километры
    distance_km = distance_m / 1000.0
    
    # Эмиссия CO2 на км для легковых автомобилей (в кг)
    emission_per_km = 0.150  # 150 г/km
    
    # Вычисление выбросов CO2
    total_emission = distance_km * emission_per_km
    return total_emission  # Возвращаем выбросы в кг
