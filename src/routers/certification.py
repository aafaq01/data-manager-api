from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload
from models.profile import Profile as ProfileModel
from ..database import get_db
from ..schemas.certification import Certification as CertificationSchema

router = APIRouter()

@router.get("/profiles/{identifier}/certifications", response_model=list[CertificationSchema])
def read_profile_certifications(identifier: str, db: Session = Depends(get_db)):
    try:
        profile_id = int(identifier)
        profile = db.query(ProfileModel).options(selectinload(ProfileModel.certifications)).filter(ProfileModel.id == profile_id).first()
    except ValueError:
        profile = db.query(ProfileModel).options(selectinload(ProfileModel.certifications)).filter(ProfileModel.name.ilike(f"%{identifier}%")).first()
    
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile.certifications
