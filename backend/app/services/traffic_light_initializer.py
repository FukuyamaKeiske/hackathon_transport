import random
import time
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.traffic_lights import TrafficLight

async def initialize_traffic_lights(db: AsyncSession):
    # Удаляем существующие светофоры, если необходимо
    await db.execute(TrafficLight.__table__.delete())

    start = (45192920, 38863628)
    end = (44974925, 39271189)

    x_min, x_max = sorted((start[0], end[0]))
    y_min, y_max = sorted((start[1], end[1]))

    for _ in range(600):
        x = random.uniform(x_min, x_max) / 1000000
        y = random.uniform(y_min, y_max) / 1000000

        red_state_duration = random.randint(30, 120)  # Увеличиваем диапазон
        green_state_duration = random.randint(10, 60)  # Увеличиваем диапазон

        new_light = TrafficLight(
            location=f"POINT({x} {y})",
            current_state="red",  # Начальное состояние
            red_state_duration=red_state_duration,
            green_state_duration=green_state_duration,
            recommended_state="red"  # Начальная рекомендация
        )
        db.add(new_light)
    
    await db.commit()
