# src/routers/certification.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from models.profile import Profile
from ..database import get_db
from ..schemas.certification import Certification as CertificationSchema

router = APIRouter()

@router.get("/profiles/{profile_id}/certifications", response_model=list[CertificationSchema])
async def read_profile_certifications(profile_id: int, db: AsyncSession = Depends(get_db)):
    # Fetch the profile with its certifications
    result = await db.execute(
        select(Profile).where(Profile.id == profile_id).options(selectinload(Profile.certifications))
    )
    profile = result.scalars().first()
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile.certifications
