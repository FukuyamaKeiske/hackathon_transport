from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.traffic_lights import TrafficLight

async def recommend_traffic_lights(db: AsyncSession):
    # Получение всех светофоров
    result = await db.execute(TrafficLight.__table__.select())
    traffic_lights = result.scalars().all()
    recommendations = []

    for light in traffic_lights:
        # Логика рекомендаций
        if light.red_state_duration >= 90 and light.green_state_duration <= 40:
            recommended_state = "Уменьшить время красного света"
        elif light.green_state_duration <= 20 and light.red_state_duration >= 60:
            recommended_state = "Увеличить время зелёного света"
        else:
            recommended_state = "Без изменений"

        recommendations.append({
            "id": light.id,
            "current_state": light.current_state,
            "recommended_action": recommended_state
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
