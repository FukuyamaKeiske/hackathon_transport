import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from app.db.base import Base  # Импортируйте ваш базовый класс
from app.core.config import settings  # Импортируйте настройки

DATABASE_URL = settings.DATABASE_URL
print(DATABASE_URL)

async def create_tables():
    engine = create_async_engine(DATABASE_URL, echo=True)

    async with engine.begin() as conn:
        # Создание всех таблиц
        await conn.run_sync(Base.metadata.create_all)

    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(create_tables())
