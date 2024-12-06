from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.traffic_analysis import get_traffic_data
from app.db.models.traffic_data import TrafficData
from pydantic import BaseModel
from typing import List, Tuple

router = APIRouter()

class Waypoint(BaseModel):
    lat: float
    lon: float

@router.post("/", response_model=dict)
async def get_traffic_analysis(
    waypoints: List[Waypoint], 
    db: AsyncSession = Depends(get_db)
):
    if not waypoints or len(waypoints) < 2:
        raise HTTPException(status_code=400, detail="At least two waypoints are required.")
    
    # Форматируем waypoints для передачи в функции
    formatted_waypoints = [(waypoint.lat, waypoint.lon) for waypoint in waypoints]
    
    traffic_data = await get_traffic_data(formatted_waypoints)
    return traffic_data
