from fastapi import FastAPI, File, UploadFile
from modules.resume_parser.parser import extract_text_from_pdf

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file)
    return {
        "filename": file.filename,
        "text": text[:1000]  # limit output for now
    }
