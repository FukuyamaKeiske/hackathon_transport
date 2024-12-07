from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.forecast_service import generate_forecasts, get_forecasts
from app.db.models.forecasts import Forecast
from pydantic import BaseModel
from typing import List, Tuple

router = APIRouter()

class ForecastRequest(BaseModel):
    waypoints: List[Tuple[float, float]]  # Список точек (широта, долгота)
    mode: str = "driving"  # Режим транспорта (по умолчанию легковой автомобиль)
    departure_time: int = None  # UNIX-время для отправления

@router.post("/", response_model=list[Forecast])
async def create_forecasts(
    forecast_request: ForecastRequest, 
    db: AsyncSession = Depends(get_db)
):
    if not forecast_request.waypoints or len(forecast_request.waypoints) < 2:
        raise HTTPException(status_code=400, detail="At least two waypoints are required.")
    
    # Генерация прогнозов на основе API
    forecasts = await generate_forecasts(forecast_request.waypoints, forecast_request.mode, forecast_request.departure_time)
    return forecasts

@router.get("/", response_model=list[Forecast])
async def list_forecasts(db: AsyncSession = Depends(get_db)):
    forecasts = await get_forecasts(db)
    return forecasts
