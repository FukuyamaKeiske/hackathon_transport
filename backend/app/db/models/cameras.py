from sqlalchemy import Column, String, Float, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2 import Geometry
from app.db.base import Base
import uuid

class Camera(Base):
    __tablename__ = "cameras"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    name = Column(String, nullable=False)
    live_url = Column(String, nullable=False)
    geo = Column(String, nullable=False)  # Например, "Москва, Россия"
    description = Column(String, nullable=True)
    location = Column(Geometry(geometry_type='POINT', srid=4326))
