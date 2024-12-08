import asyncio
from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
from app.db.base import Base
from app.db.models import *  # Импортируйте все ваши модели
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

# Конфигурация Alembic
config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(run_migrations)

def run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()

def main():
    """Run migrations based on context mode."""
    if context.is_offline_mode():
        run_migrations_offline()
    else:
        asyncio.run(run_migrations_online())

main()
