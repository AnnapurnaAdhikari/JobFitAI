# 🚀 AI Career Assistant

An AI-powered platform that analyzes resumes and recommends relevant job roles based on extracted skills.

---

## 🔄 System Flow

Upload Resume
↓
Extract Text
↓
Extract Skills
↓
Match Jobs *(coming next)*
↓
Show Results

---

## ✅ MVP Features

* 📄 Resume Upload (PDF → Text)
* 🧠 Skill Extraction (Text → Skills)
* 🎯 Job Recommendation *(in progress)*

---

## ⚙️ What’s Implemented

* FastAPI backend setup
* Resume upload API
* PDF text extraction
* Dynamic skill extraction using real-world dataset
* Modular project structure (feature-based)

---

## 🔗 API Endpoint

### Upload Resume

```http
POST /upload-resume
```

### Example (Local)

```
http://127.0.0.1:8000/upload-resume
```

### Response

```json
{
  "filename": "resume.pdf",
  "skills": ["python", "sql", "machine learning"],
  "text_preview": "..."
}
```

---

## 🛠️ Tech Stack

* Backend: FastAPI
* NLP: Basic text + dataset-driven matching
* Data: Custom skills dataset

---

## 📌 Current Status

✅ Resume parsing
✅ Skill extraction
🔄 Job matching (next step)

---

## 🚀 Next Steps

* Job Recommendation Engine
* Skill Gap Analyzer
* Interview Question Generator
* AI Mock Interview System

---
