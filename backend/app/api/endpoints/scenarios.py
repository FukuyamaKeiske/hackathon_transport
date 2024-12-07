from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.scenario_simulation import simulate_scenarios, add_scenario
from app.db.schemas.scenarios import Scenario  # Импортируем Pydantic модель

router = APIRouter()

@router.get("/", response_model=list[Scenario])
async def list_scenarios(db: AsyncSession = Depends(get_db)):
    scenarios = await simulate_scenarios(db)
    return scenarios

@router.post("/", response_model=Scenario)
async def create_scenario(scenario_data: Scenario, db: AsyncSession = Depends(get_db)):
    new_scenario = await add_scenario(db, scenario_data.dict())
    return new_scenario
