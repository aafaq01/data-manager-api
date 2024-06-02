from fastapi import FastAPI, HTTPException
from .routers import profile, certification, past_experience

app = FastAPI()

@app.get("/health")
async def root():
    return {"message": "Healthy"}

app.include_router(profile.router, prefix="/api")
app.include_router(certification.router, prefix="/api")
app.include_router(past_experience.router, prefix="/api")