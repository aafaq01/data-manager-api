# src/routers/programming_skill.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from models.profile import Profile as ProfileModel
from ..database import get_db
from ..schemas.programming_skill import ProgrammingSkill as ProgrammingSkillSchema

router = APIRouter()

@router.get("/profiles/{profile_identifier}/programming_skills", response_model=list[ProgrammingSkillSchema])
def read_profile_programming_skills(profile_identifier: str, db: Session = Depends(get_db)):
    profile = db.query(ProfileModel).options(selectinload(ProfileModel.programming_skills)).filter(
        (ProfileModel.id == profile_identifier) | (ProfileModel.name == profile_identifier)
    ).first()
    
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile.programming_skills
