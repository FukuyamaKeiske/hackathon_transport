from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.events import Event

async def get_events(db: AsyncSession):
    result = await db.execute(Event.__table__.select())
    return result.scalars().all()

async def add_event(db: AsyncSession, event_data: dict):
    new_event = Event(
        name=event_data['name'],
        date=event_data['date'],
        location=f"POINT({event_data['longitude']} {event_data['latitude']})",
        impact_level=event_data.get('impact_level', 1)
    )
    db.add(new_event)
    await db.commit()
    return new_event
