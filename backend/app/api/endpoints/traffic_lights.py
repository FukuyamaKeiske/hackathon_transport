from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.traffic_light_recommendations import recommend_traffic_lights, update_traffic_light_state
from app.db.models.traffic_lights import TrafficLight

router = APIRouter()

@router.get("/recommendations", response_model=list[dict])
async def get_recommendations(db: AsyncSession = Depends(get_db)):
    recommendations = await recommend_traffic_lights(db)
    return recommendations

@router.put("/{light_id}", response_model=TrafficLight)
async def change_traffic_light_state(light_id: str, new_state: str, db: AsyncSession = Depends(get_db)):
    updated_light = await update_traffic_light_state(db, light_id, new_state)
    if updated_light is None:
        raise HTTPException(status_code=404, detail="Traffic light not found")
    return updated_light
