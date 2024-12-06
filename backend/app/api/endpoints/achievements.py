from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.achievement_tracking import get_achievements, add_achievement
from app.db.models.achievements import Achievement

router = APIRouter()

@router.get("/", response_model=list[Achievement])
async def list_achievements(db: AsyncSession = Depends(get_db)):
    achievements = await get_achievements(db)
    return achievements

@router.post("/", response_model=Achievement)
async def create_achievement(achievement_data: dict, db: AsyncSession = Depends(get_db)):
    new_achievement = await add_achievement(db, achievement_data)
    return new_achievement
