from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.effectiveness_analysis import analyze_effectiveness, add_effectiveness_measure
from app.db.models.effectiveness import Effectiveness

router = APIRouter()

@router.get("/", response_model=list[Effectiveness])
async def list_effectiveness(db: AsyncSession = Depends(get_db)):
    effectiveness_data = await analyze_effectiveness(db)
    return effectiveness_data

@router.post("/", response_model=Effectiveness)
async def create_effectiveness(measure_data: dict, db: AsyncSession = Depends(get_db)):
    new_measure = await add_effectiveness_measure(db, measure_data)
    return new_measure
