# src/schemas/soft_skill.py

from pydantic import BaseModel
from typing import Optional

class SoftSkillBase(BaseModel):
    name: str
    description: Optional[str]

class SoftSkill(SoftSkillBase):
    class Config:
        orm_mode = True
