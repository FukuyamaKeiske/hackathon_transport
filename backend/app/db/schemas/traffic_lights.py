from pydantic import BaseModel
from uuid import UUID

class TrafficLightBase(BaseModel):
    location: str  # Формат: "POINT(lon lat)"
    current_state: str
    recommended_state: str
    red_state_duration: int
    green_state_duration: int

class TrafficLightCreate(TrafficLightBase):
    pass

class TrafficLight(TrafficLightBase):
    id: UUID

    class Config:
        from_attributes = True  # Обновлено для Pydantic V2
