from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class ForecastBase(BaseModel):
    timestamp: datetime
    location: str  # Например, "POINT(lon lat)"
    predicted_density: int
    predicted_speed: float

class ForecastCreate(ForecastBase):
    pass

class Forecast(ForecastBase):
    id: UUID

    class Config:
        orm_mode = True
