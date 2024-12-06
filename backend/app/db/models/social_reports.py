from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2 import Geometry
from app.db.base import Base

class SocialReport(Base):
    __tablename__ = "social_reports"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    timestamp = Column(TIMESTAMP, nullable=False)
    location = Column(Geometry(geometry_type='POINT', srid=4326))
    content = Column(String)
    source = Column(String)
