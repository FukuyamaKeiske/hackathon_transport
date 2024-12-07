from pydantic import BaseModel
from uuid import UUID
from typing import Any

class ScenarioBase(BaseModel):
    name: str
    description: str
    impact_assessment: Any  # Замените на конкретный тип, если известно

class ScenarioCreate(ScenarioBase):
    pass

class Scenario(ScenarioBase):
    id: UUID

    class Config:
        orm_mode = True
