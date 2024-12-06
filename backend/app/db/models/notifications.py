from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    timestamp = Column(TIMESTAMP, nullable=False)
    driver_id = Column(UUID(as_uuid=True))
    message = Column(String)
