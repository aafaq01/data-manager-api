# src/routers/profile.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.profile import Profile as ProfileModel
from ..database import get_db
from ..schemas.profile import Profile as ProfileSchema

router = APIRouter()

@router.get("/profiles", response_model=list[ProfileSchema])
async def read_profiles(
    skip: int = 0,
    limit: int = 10,
    name: str = Query(None),
    db: AsyncSession = Depends(get_db)
):
    query = select(ProfileModel)
    
    if name:
        query = query.where(ProfileModel.name.ilike(f"%{name}%"))

    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    profiles = result.scalars().all()
    return profiles

@router.get("/profiles/{profile_id}", response_model=ProfileSchema)
async def read_profile(profile_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ProfileModel).where(ProfileModel.id == profile_id))
    profile = result.scalars().first()
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
