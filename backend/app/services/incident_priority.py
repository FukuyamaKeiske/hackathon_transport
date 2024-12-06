from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.incidents import Incident

async def get_incidents(db: AsyncSession):
    result = await db.execute(Incident.__table__.select())
    incidents = result.scalars().all()
    
    # Логика для приоритизации инцидентов
    prioritized_incidents = sorted(incidents, key=lambda x: x.severity, reverse=True)
    return prioritized_incidents

async def get_incident_by_id(db: AsyncSession, incident_id: str):
    result = await db.execute(Incident.__table__.select().where(Incident.id == incident_id))
    return result.scalar_one_or_none()
