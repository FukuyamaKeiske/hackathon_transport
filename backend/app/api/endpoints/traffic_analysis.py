from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.traffic_analysis import analyze_traffic
from app.db.models.traffic_data import TrafficData

router = APIRouter()

@router.post("/", response_model=list[TrafficData])
async def get_traffic_analysis(db: AsyncSession = Depends(get_db)):
    traffic_data = await analyze_traffic(db)
    return traffic_data
