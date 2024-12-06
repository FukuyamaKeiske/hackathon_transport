from sqlalchemy import Column, Float, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2 import Geometry
from app.db.base import Base

class EnvironmentalData(Base):
    __tablename__ = "environmental_data"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    timestamp = Column(TIMESTAMP, nullable=False)
    location = Column(Geometry(geometry_type='POINT', srid=4326))
    emission_level = Column(Float)
