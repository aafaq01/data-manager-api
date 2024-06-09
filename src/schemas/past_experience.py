# src/schemas/past_experience.py

from pydantic import BaseModel

class PastExperienceBase(BaseModel):
    title: str
    company: str
    description: str
    start_date: str
    end_date: str | None = None

class PastExperience(PastExperienceBase):

    class Config:
        orm_mode = True
