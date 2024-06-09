# src/routers/project.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from models.profile import Profile as ProfileModel
from ..database import get_db
from ..schemas.project import Project as ProjectSchema

router = APIRouter()

@router.get("/profiles/{profile_identifier}/projects", response_model=list[ProjectSchema])
def read_profile_projects(profile_identifier: str, db: Session = Depends(get_db)):
    profile = db.query(ProfileModel).options(selectinload(ProfileModel.projects)).filter(
        (ProfileModel.id == profile_identifier) | (ProfileModel.name == profile_identifier)
    ).first()
    
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile.projects
