# src/schemas/tech_stack.py

from pydantic import BaseModel
from typing import Optional

class TechStackBase(BaseModel):
    name: str
    description: Optional[str]

class TechStack(TechStackBase):
    class Config:
        orm_mode = True
