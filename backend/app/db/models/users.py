from sqlalchemy import (
    Column,
    String
)

from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    email = Column(String, nullable=False)
    jwt_token = Column(String, nullable=False)
