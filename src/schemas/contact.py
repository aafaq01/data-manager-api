# src/schemas/contact.py

from pydantic import BaseModel
from typing import Optional

class ContactBase(BaseModel):
    email: str
    phone: str
    address: Optional[str] = None  # Make address optional

class Contact(ContactBase):
    class Config:
        orm_mode = True
