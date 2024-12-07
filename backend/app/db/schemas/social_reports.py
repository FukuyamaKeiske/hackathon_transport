from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class SocialReportBase(BaseModel):
    timestamp: datetime
    location: str  # Например, "POINT(lon lat)"
    content: str
    source: str

class SocialReportCreate(SocialReportBase):
    pass

class SocialReport(SocialReportBase):
    id: UUID

    class Config:
        orm_mode = True  # Позволяет использовать SQLAlchemy модели
