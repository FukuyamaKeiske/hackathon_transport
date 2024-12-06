from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.effectiveness import Effectiveness

async def analyze_effectiveness(db: AsyncSession):
    result = await db.execute(Effectiveness.__table__.select())
    return result.scalars().all()

async def add_effectiveness_measure(db: AsyncSession, measure_data: dict):
    new_effectiveness = Effectiveness(
        measure_id=measure_data['measure_id'],
        before=measure_data['before'],
        after=measure_data['after'],
        effectiveness_score=measure_data['effectiveness_score']
    )
    db.add(new_effectiveness)
    await db.commit()
    return new_effectiveness
