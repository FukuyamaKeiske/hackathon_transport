import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.exc import SQLAlchemyError
from app.db.base import Base  # Импортируйте ваш базовый класс
from app.core.config import settings  # Импортируйте настройки
from app.db.models.achievements import Achievement
from app.db.models.cameras import Camera
from app.db.models.effectiveness import Effectiveness
from app.db.models.environmental_data import EnvironmentalData
from app.db.models.events import Event
from app.db.models.forecasts import Forecast
from app.db.models.incidents import Incident
from app.db.models.notifications import Notification
from app.db.models.scenarios import Scenario
from app.db.models.social_reports import SocialReport
from app.db.models.traffic_data import TrafficData
from app.db.models.traffic_lights import TrafficLight
from app.db.models.users import User

print(Base.metadata)

DATABASE_URL = settings.DATABASE_URL

async def create_tables():
    # Создаем асинхронный движок
    engine = create_async_engine(DATABASE_URL, echo=True)

    try:
        # Создаем все таблицы асинхронно
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("Таблицы успешно созданы.")
    except SQLAlchemyError as e:
        print(f"Ошибка при создании таблиц: {e}")
    finally:
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(create_tables())
