from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class NotificationBase(BaseModel):
    timestamp: datetime
    driver_id: UUID
    message: str

class NotificationCreate(NotificationBase):
    pass

class Notification(NotificationBase):
    id: UUID

    class Config:
        orm_mode = True  # Позволяет использовать SQLAlchemy модели
