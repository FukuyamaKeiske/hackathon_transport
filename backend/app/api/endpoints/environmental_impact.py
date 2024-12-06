from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.environmental_impact import get_environmental_data, add_environmental_data
from app.db.models.environmental_data import EnvironmentalData

router = APIRouter()

@router.get("/", response_model=list[EnvironmentalData])
async def list_environmental_data(db: AsyncSession = Depends(get_db)):
    environmental_data = await get_environmental_data(db)
    return environmental_data

@router.post("/", response_model=EnvironmentalData)
async def create_environmental_data(data: dict, db: AsyncSession = Depends(get_db)):
    new_data = await add_environmental_data(db, data)
    return new_data
