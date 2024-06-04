# src/routers/resume.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from models.profile import Profile as ProfileModel
from ..database import get_db
from ..schemas.tech_stack import TechStack as TechStackSchema

router = APIRouter()

@router.get("/profiles/{profile_identifier}/tech_stacks", response_model=list[TechStackSchema])
def read_profile_resume(profile_identifier: str, db: Session = Depends(get_db)):
    profile = db.query(ProfileModel).options(selectinload(ProfileModel.tech_stacks)).filter(
        (ProfileModel.id == profile_identifier) | (ProfileModel.name == profile_identifier)
    ).first()
    
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile.tech_stacks
