from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.scenarios import Scenario

async def simulate_scenarios(db: AsyncSession):
    result = await db.execute(Scenario.__table__.select())
    return result.scalars().all()

async def add_scenario(db: AsyncSession, scenario_data: dict):
    new_scenario = Scenario(
        name=scenario_data['name'],
        description=scenario_data['description'],
        impact_assessment=scenario_data['impact_assessment']
    )
    db.add(new_scenario)
    await db.commit()
    return new_scenario
