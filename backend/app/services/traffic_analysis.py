import httpx
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.traffic_data import TrafficData
from app.core.config import settings

async def analyze_traffic(db: AsyncSession):
    # Запрос к API Яндекс Карт (примерный URL)
    response = await httpx.get("https://api.yandex.com/traffic")
    response.raise_for_status()  # Проверка на ошибки

    traffic_info = response.json()
    traffic_data = []

    for data in traffic_info.get('data', []):
        traffic_data.append(TrafficData(
            timestamp=data['timestamp'],
            location=f"POINT({data['longitude']} {data['latitude']})",
            density=data['density'],
            speed=data['speed']
        ))

    db.add_all(traffic_data)
    await db.commit()
    return traffic_data
