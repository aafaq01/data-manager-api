from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, selectinload
from models.profile import Profile as ProfileModel
from ..database import get_db
from ..schemas.profile import Profile, ProfileCreate, ProfileDetail

router = APIRouter()

@router.get("/profiles", response_model=list[Profile])
def read_profiles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    profiles = db.query(ProfileModel).offset(skip).limit(limit).all()
    return profiles

@router.get("/profiles/{profile_id}", response_model=Profile)
def read_profile(profile_id: int, db: Session = Depends(get_db)):
    profile = db.query(ProfileModel).filter(ProfileModel.id == profile_id).first()
    
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    return profile

@router.get("/profiles/{profile_id}/details", response_model=ProfileDetail)
def read_profile_details(profile_id: int, db: Session = Depends(get_db)):
    profile = db.query(ProfileModel).options(
        selectinload(ProfileModel.certifications),
        selectinload(ProfileModel.contacts),
        selectinload(ProfileModel.past_experiences),
        selectinload(ProfileModel.programming_skills),
        selectinload(ProfileModel.projects),
        selectinload(ProfileModel.resumes),
        selectinload(ProfileModel.soft_skills),
        selectinload(ProfileModel.tech_stacks)
    ).filter(ProfileModel.id == profile_id).first()
    
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    return profile

@router.post("/profiles", response_model=Profile)
def create_profile(profile: ProfileCreate, db: Session = Depends(get_db)):

    existing_profile = db.query(ProfileModel).filter(ProfileModel.name.ilike(profile.name)).first()
    if existing_profile:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Profile with this name already exists.")
    
    db_profile = ProfileModel(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile
