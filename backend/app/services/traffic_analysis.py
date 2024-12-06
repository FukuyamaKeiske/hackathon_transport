import httpx
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import settings

async def get_traffic_data(waypoints: list):
    # Яндекс Карт
    yandex_url = "https://api.routing.yandex.net/v2/route"
    yandex_params = {
        "apikey": settings.YANDEX_MAPS_API_KEY,
        "waypoints": "|".join(waypoints),
        "mode": "driving",
        "traffic": "realtime"
    }
    
    async with httpx.AsyncClient() as client:
        yandex_response = await client.get(yandex_url, params=yandex_params)
        yandex_data = yandex_response.json()

    # 2ГИС
    twogis_url = "http://routing.api.2gis.com/routing/7.0.0/global"
    twogis_payload = {
        "points": [{"type": "stop", "lon": float(lon), "lat": float(lat)} for lat, lon in waypoints],
        "transport": "driving",
        "route_mode": "fastest",
        "traffic_mode": "jam"
    }
    
    async with httpx.AsyncClient() as client:
        twogis_response = await client.post(twogis_url, json=twogis_payload)
        twogis_data = twogis_response.json()

    return {"yandex": yandex_data, "twogis": twogis_data}
