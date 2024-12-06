from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.traffic_lights import TrafficLight

async def recommend_traffic_lights(db: AsyncSession):
    # Логика для получения рекомендаций по светофорам
    traffic_lights = await db.execute(TrafficLight.__table__.select())
    recommendations = []

    for light in traffic_lights.scalars().all():
        # Пример логики для рекомендаций
        recommended_state = "green" if light.current_state == "red" else "red"
        recommendations.append({
            "id": light.id,
            "current_state": light.current_state,
            "recommended_state": recommended_state
        })

    return recommendations

async def update_traffic_light_state(db: AsyncSession, light_id: str, new_state: str):
    result = await db.execute(TrafficLight.__table__.select().where(TrafficLight.id == light_id))
    traffic_light = result.scalar_one_or_none()
    
    if traffic_light:
        traffic_light.current_state = new_state
        await db.commit()
        return traffic_light
    return None
