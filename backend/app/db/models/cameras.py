from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2 import Geometry
from app.db.base import Base

class Camera(Base):
    __tablename__ = "cameras"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    location = Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    url = Column(String, nullable=False)
    status = Column(Boolean, default=True)
