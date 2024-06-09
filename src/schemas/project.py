# src/schemas/project.py

from pydantic import BaseModel
from typing import Optional

class ProjectBase(BaseModel):
    name: str
    description: Optional[str]
    url: Optional[str] = None

class Project(ProjectBase):
    class Config:
        orm_mode = True
