from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from models.profile import Profile as ProfileModel
from ..database import get_db
from ..schemas.profile import Profile as ProfileSchema

router = APIRouter()

@router.get("/profiles", response_model=list[ProfileSchema])
def read_profiles(
    skip: int = 0,
    limit: int = 10,
    name: str = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(ProfileModel)
    
    if name:
        query = query.filter(ProfileModel.name.ilike(f"%{name}%"))

    profiles = query.offset(skip).limit(limit).all()
    return profiles

@router.get("/profiles/{profile_id}", response_model=ProfileSchema)
def read_profile(profile_id: int, db: Session = Depends(get_db)):
    profile = db.query(ProfileModel).filter(ProfileModel.id == profile_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
