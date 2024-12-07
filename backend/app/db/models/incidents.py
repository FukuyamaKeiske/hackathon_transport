from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    description = Column(String, nullable=False)
    severity = Column(Integer, nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)
    location = Column(String, nullable=True)  # Например, "Москва, Россия"

    # Добавьте метод для преобразования в словарь, если требуется
    def to_dict(self):
        return {
            "id": str(self.id),
            "description": self.description,
            "severity": self.severity,
            "timestamp": self.timestamp.isoformat(),
            "location": self.location
        }
