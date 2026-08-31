from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Resume Analyzer API is running"}

class ResumeInfo(BaseModel):
    name: str
    email: str
    phone: str


@app.post("/resume")
async def create_resume(resume: ResumeInfo):
    return resume