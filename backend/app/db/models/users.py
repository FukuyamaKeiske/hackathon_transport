from sqlalchemy import (
    Column,
    String
)

from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    email = Column(String, nullable=False)
    jwt_token = Column(String, nullable=False)
