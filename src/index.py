from fastapi import FastAPI, HTTPException
from .routers import profile, certification

app = FastAPI()

@app.get("/health")
async def root():
    return {"message": "Healthy"}

app.include_router(profile.router, prefix="/api")
app.include_router(certification.router, prefix="/api")