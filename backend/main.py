from fastapi import FastAPI, File, UploadFile
from modules.resume_parser.parser import extract_text_from_pdf
from modules.skill_analyzer.skill_extractor import extract_skills
from modules.job_matcher.matcher import match_jobs

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    # Step 1: Extract text
    text = extract_text_from_pdf(file)

    # Step 2: Extract skills
    skills = extract_skills(text)

    # Step 3: Match jobs
    jobs = match_jobs(skills)

    return {
        "filename": file.filename,
        "skills": skills,
        "recommended_jobs": jobs
    }