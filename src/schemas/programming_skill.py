# src/schemas/contact.py

from pydantic import BaseModel

class ProgrammingSkillBase(BaseModel):
    name: str
    level: str

class ProgrammingSkill(ProgrammingSkillBase):
    class Config:
        orm_mode = True
