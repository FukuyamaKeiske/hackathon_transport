from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class TrafficLightBase(BaseModel):
    location: str  # Формат: "POINT(lon lat)"
    current_state: str
    recommended_state: str

class TrafficLightCreate(TrafficLightBase):
    pass

class TrafficLight(TrafficLightBase):
    id: UUID

    class Config:
        orm_mode = True
