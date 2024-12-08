from sqlalchemy import Column, Integer, Float, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2 import Geometry
from app.db.base import Base
import uuid

class Forecast(Base):
    __tablename__ = "forecast_data"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    timestamp = Column(TIMESTAMP, nullable=False)
    location = Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    predicted_density = Column(Integer)
    predicted_speed = Column(Float)
