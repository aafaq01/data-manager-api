# src/schemas/profile.py

from pydantic import BaseModel

class ProfileBase(BaseModel):
    name: str
    description: str

class CertificationCreate(ProfileBase):
    id: int

class Profile(ProfileBase):

    class Config:
        orm_mode = True
