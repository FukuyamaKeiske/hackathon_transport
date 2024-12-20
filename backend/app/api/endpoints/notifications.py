from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.driver_notifications import get_notifications, add_notification
from app.db.schemas.notifications import Notification  # Импортируем Pydantic модель

router = APIRouter()

@router.get("/", response_model=list[Notification])
async def list_notifications(db: AsyncSession = Depends(get_db)):
    notifications = await get_notifications(db)
    return notifications

@router.post("/", response_model=Notification)
async def create_notification(notification_data: Notification, db: AsyncSession = Depends(get_db)):
    new_notification = await add_notification(db, notification_data.dict())
    return new_notification
