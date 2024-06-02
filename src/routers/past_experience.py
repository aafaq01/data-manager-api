# src/routers/past_experience.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from models.profile import Profile as ProfileModel
from ..database import get_db
from ..schemas.past_experience import PastExperience as PastExperienceSchema

router = APIRouter()

@router.get("/profiles/{identifier}/past_experiences", response_model=list[PastExperienceSchema])
def read_profile_past_experiences(identifier: str, db: Session = Depends(get_db)):
    try:
        profile_id = int(identifier)
        profile = db.query(ProfileModel).options(selectinload(ProfileModel.past_experiences)).filter(ProfileModel.id == profile_id).first()
    except ValueError:
        profile = db.query(ProfileModel).options(selectinload(ProfileModel.past_experiences)).filter(ProfileModel.name.ilike(f"%{identifier}%")).first()
    
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile.past_experiences
