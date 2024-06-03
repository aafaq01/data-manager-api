from fastapi import FastAPI, HTTPException
from .routers import profile, certification, past_experience, contact, programming_skill, project, resume

app = FastAPI()

@app.get("/health")
async def root():
    return {"message": "Healthy"}

app.include_router(profile.router, prefix="/api")
app.include_router(certification.router, prefix="/api")
app.include_router(past_experience.router, prefix="/api")
app.include_router(contact.router, prefix="/api")
app.include_router(programming_skill.router, prefix="/api")
app.include_router(project.router, prefix="/api")
app.include_router(resume.router, prefix="/api")