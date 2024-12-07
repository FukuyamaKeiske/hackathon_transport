from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class AchievementBase(BaseModel):
    operator_id: UUID
    achievement_type: str
    timestamp: datetime

class AchievementCreate(AchievementBase):
    pass

class Achievement(AchievementBase):
    id: UUID

    class Config:
        orm_mode = True  # Позволяет использовать SQLAlchemy модели
