from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class EventBase(BaseModel):
    name: str
    date: datetime
    location: str  # Например, "POINT(lon lat)"
    impact_level: int

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: UUID

    class Config:
        orm_mode = True
