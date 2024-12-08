from sqlalchemy import Column, Float, JSON
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid

class Effectiveness(Base):
    __tablename__ = "effectiveness"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    measure_id = Column(UUID(as_uuid=True), nullable=False)
    before = Column(JSON)
    after = Column(JSON)
    effectiveness_score = Column(Float)
