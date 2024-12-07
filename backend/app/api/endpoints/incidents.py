from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.incident_priority import get_incidents, get_incident_by_id
from app.db.models.incidents import Incident

router = APIRouter()

@router.get("/", response_model=list[dict])
async def list_incidents(db: AsyncSession = Depends(get_db)):
    incidents = await get_incidents(db)
    return [incident.to_dict() for incident in incidents]  # Используем метод to_dict

@router.get("/{incident_id}", response_model=dict)
async def read_incident(incident_id: str, db: AsyncSession = Depends(get_db)):
    incident = await get_incident_by_id(db, incident_id)
    if incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident.to_dict()  # Используем метод to_dict
