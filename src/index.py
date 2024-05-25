# src/index.py
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/health")
async def root():
    return {"message": "Healthy"}