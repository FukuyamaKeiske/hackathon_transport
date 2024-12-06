from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.forecast_service import generate_forecasts, get_forecasts
from app.db.models.forecasts import Forecast

router = APIRouter()

@router.post("/", response_model=list[Forecast])
async def create_forecasts(db: AsyncSession = Depends(get_db)):
    forecasts = await generate_forecasts(db)
    return forecasts

@router.get("/", response_model=list[Forecast])
async def list_forecasts(db: AsyncSession = Depends(get_db)):
    forecasts = await get_forecasts(db)
    return forecasts
