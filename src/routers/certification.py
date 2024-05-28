from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload
from models.profile import Profile as ProfileModel
from ..database import get_db
from ..schemas.certification import Certification as CertificationSchema

router = APIRouter()

@router.get("/profiles/{profile_id}/certifications", response_model=list[CertificationSchema])
def read_profile_certifications(profile_id: int, db: Session = Depends(get_db)):
    # Fetch the profile with its certifications
    profile = db.query(ProfileModel).options(selectinload(ProfileModel.certifications)).filter(ProfileModel.id == profile_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile.certifications
