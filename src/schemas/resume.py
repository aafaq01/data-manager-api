# src/schemas/resume.py

from pydantic import BaseModel

class ResumeBase(BaseModel):
    file_path: str

class Resume(ResumeBase):
    class Config:
        orm_mode = True
