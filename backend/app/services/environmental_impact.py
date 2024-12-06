from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.environmental_data import EnvironmentalData

async def get_environmental_data(db: AsyncSession):
    result = await db.execute(EnvironmentalData.__table__.select())
    return result.scalars().all()

async def add_environmental_data(db: AsyncSession, environmental_data: dict):
    new_data = EnvironmentalData(
        timestamp=environmental_data['timestamp'],
        location=f"POINT({environmental_data['longitude']} {environmental_data['latitude']})",
        emission_level=environmental_data['emission_level']
    )
    db.add(new_data)
    await db.commit()
    return new_data
