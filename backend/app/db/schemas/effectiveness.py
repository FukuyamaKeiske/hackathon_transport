from pydantic import BaseModel
from uuid import UUID
from typing import Any
from datetime import datetime

class EffectivenessBase(BaseModel):
    measure_id: UUID
    before: Any  # Замените на конкретный тип, если известно
    after: Any   # Замените на конкретный тип, если известно
    effectiveness_score: float

class EffectivenessCreate(EffectivenessBase):
    pass

class Effectiveness(EffectivenessBase):
    id: UUID
    timestamp: datetime  # Если необходимо

    class Config:
        orm_mode = True
