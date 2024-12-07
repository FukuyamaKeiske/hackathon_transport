from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.event_notifications import get_events, add_event
from app.db.models.events import Event

router = APIRouter()

@router.get("/", response_model=list[Event])
async def list_events(db: AsyncSession = Depends(get_db)):
    events = await get_events(db)
    return events

@router.post("/", response_model=Event)
async def create_event(event_data: dict, db: AsyncSession = Depends(get_db)):
    new_event = await add_event(db, event_data)
    return new_event