# src/routers/contact.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from models.profile import Profile as ProfileModel
from ..database import get_db
from ..schemas.contact import Contact as ContactSchema

router = APIRouter()

@router.get("/profiles/{profile_identifier}/contacts", response_model=list[ContactSchema])
def read_profile_contacts(profile_identifier: str, db: Session = Depends(get_db)):
    # Fetch the profile with its contacts by ID or name
    profile = db.query(ProfileModel).options(selectinload(ProfileModel.contacts)).filter(
        (ProfileModel.id == profile_identifier) | (ProfileModel.name == profile_identifier)
    ).first()
    
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile.contacts
