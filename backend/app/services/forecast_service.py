from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.forecasts import Forecast
import random
from datetime import datetime

async def generate_forecasts(db: AsyncSession):
    # Пример генерации прогнозов
    forecasts = []
    for _ in range(10):  # Генерируем 10 прогнозов
        forecast = Forecast(
            timestamp=datetime.now(),
            location="POINT({} {})".format(random.uniform(-180, 180), random.uniform(-90, 90)),
            predicted_density=random.randint(0, 100),
            predicted_speed=random.uniform(0, 120)
        )
        forecasts.append(forecast)

    db.add_all(forecasts)
    await db.commit()
    return forecasts

async def get_forecasts(db: AsyncSession):
    result = await db.execute(Forecast.__table__.select())
    return result.scalars().all()
