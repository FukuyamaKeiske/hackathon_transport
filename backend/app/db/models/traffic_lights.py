from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2 import Geometry
from app.db.base import Base

class TrafficLight(Base):
    __tablename__ = "traffic_lights"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    location = Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    current_state = Column(String, nullable=False)
    recommended_state = Column(String)
