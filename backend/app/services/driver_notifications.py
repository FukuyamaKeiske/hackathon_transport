from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.notifications import Notification

async def get_notifications(db: AsyncSession):
    result = await db.execute(Notification.__table__.select())
    return result.scalars().all()

async def add_notification(db: AsyncSession, notification_data: dict):
    new_notification = Notification(
        timestamp=notification_data['timestamp'],
        driver_id=notification_data['driver_id'],
        message=notification_data['message']
    )
    db.add(new_notification)
    await db.commit()
    return new_notification
