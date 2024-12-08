from sqlalchemy import Column, String, Integer, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2 import Geometry
from app.db.base import Base
import uuid

class TrafficLight(Base):
    __tablename__ = "traffic_lights"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    location = Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    current_state = Column(String, nullable=False)
    red_state_duration = Column(Integer, nullable=False)
    green_state_duration = Column(Integer, nullable=False)
    recommended_state = Column(String)
    created_at = Column(TIMESTAMP, default=func.now(), nullable=False)
