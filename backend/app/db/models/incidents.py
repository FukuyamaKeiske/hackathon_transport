from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2 import Geometry
from app.db.base import Base

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    timestamp = Column(TIMESTAMP, nullable=False)
    location = Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    severity = Column(Integer, nullable=False)
    description = Column(String)
