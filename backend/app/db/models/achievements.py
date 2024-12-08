from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid

class Achievement(Base):
    __tablename__ = "achievements"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    operator_id = Column(UUID(as_uuid=True), nullable=False)
    achievement_type = Column(String, nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)
