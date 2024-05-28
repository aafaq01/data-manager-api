# src/schemas/certification.py

from pydantic import BaseModel
from datetime import date

class CertificationBase(BaseModel):
    name: str
    issuing_organization: str
    issue_date: date
    expiration_date: date | None = None

class CertificationCreate(CertificationBase):
    profile_id: int
    id: int

class Certification(CertificationBase):

    class Config:
        orm_mode = True
