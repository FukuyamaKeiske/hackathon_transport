from sqlalchemy import Column, Integer, Float, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2 import Geometry
from app.db.base import Base
import uuid

class TrafficData(Base):
    __tablename__ = "traffic_data"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    timestamp = Column(TIMESTAMP, nullable=False)
    location = Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    density = Column(Integer)
    speed = Column(Float)
