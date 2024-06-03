# src/routers/resume.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from models.profile import Profile as ProfileModel
from ..database import get_db
from ..schemas.soft_skill import SoftSkill as SoftSkillSchema

router = APIRouter()

@router.get("/profiles/{profile_identifier}/soft_skills", response_model=list[SoftSkillSchema])
def read_profile_resume(profile_identifier: str, db: Session = Depends(get_db)):
    profile = db.query(ProfileModel).options(selectinload(ProfileModel.soft_skills)).filter(
        (ProfileModel.id == profile_identifier) | (ProfileModel.name == profile_identifier)
    ).first()
    
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile.soft_skills
