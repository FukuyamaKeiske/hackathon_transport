from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class EnvironmentalDataBase(BaseModel):
    timestamp: datetime
    location: str  # Например, "POINT(lon lat)"
    emission_level: float

class EnvironmentalDataCreate(EnvironmentalDataBase):
    pass

class EnvironmentalData(EnvironmentalDataBase):
    id: UUID

    class Config:
        orm_mode = True  # Позволяет использовать SQLAlchemy модели
