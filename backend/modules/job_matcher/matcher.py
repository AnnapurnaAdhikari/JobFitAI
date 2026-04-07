import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
JOBS_PATH = os.path.join(BASE_DIR, "data", "job_dataset.json")

def load_jobs():
    with open(JOBS_PATH, "r") as f:
        return json.load(f)

JOBS_DB = load_jobs()


def match_jobs(user_skills):
    results = []

    user_skills = set([s.lower() for s in user_skills])

    for job in JOBS_DB:
        job_skills = set([s.lower() for s in job.get("Skills", [])])
        job_keywords = set([k.lower() for k in job.get("Keywords", [])])

        # Combine both
        combined = job_skills.union(job_keywords)

        matched = user_skills.intersection(combined)

        if len(combined) == 0:
            continue

        score = len(matched) / len(combined)

        results.append({
            "job_title": job["Title"],
            "match_score": round(score, 2),
            "matched_skills": list(matched)
        })

    return sorted(results, key=lambda x: x["match_score"], reverse=True)[:5]