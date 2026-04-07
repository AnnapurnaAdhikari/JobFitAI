from fastapi import FastAPI, File, UploadFile
from modules.resume_parser.parser import extract_text_from_pdf
from modules.skill_analyzer.skill_extractor import extract_skills

app = FastAPI()

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file)
    skills = extract_skills(text)

    return {
        "filename": file.filename,
        "skills": skills,
        "text_preview": text[:1000]
    }