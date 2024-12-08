from sqlalchemy import Column, String, JSON
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid

class Scenario(Base):
    __tablename__ = "scenarios"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    impact_assessment = Column(JSON)
