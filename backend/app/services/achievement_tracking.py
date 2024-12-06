from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.achievements import Achievement

async def get_achievements(db: AsyncSession):
    result = await db.execute(Achievement.__table__.select())
    return result.scalars().all()

async def add_achievement(db: AsyncSession, achievement_data: dict):
    new_achievement = Achievement(
        operator_id=achievement_data['operator_id'],
        achievement_type=achievement_data['achievement_type'],
        timestamp=achievement_data['timestamp']
    )
    db.add(new_achievement)
    await db.commit()
    return new_achievement
