import json
import os

# Get base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
SKILLS_PATH = os.path.join(BASE_DIR, "data", "skills_flat.json")

def load_skills():
    with open(SKILLS_PATH, "r") as f:
        return json.load(f)

SKILLS_DB = load_skills()


ALIASES = {
    "ml": "machine learning",
    "dl": "deep learning",
    "js": "javascript",
    "HTML/CSS": ["HTML", "CSS"]
}

def extract_skills(text):
    text = text.lower()
    found_skills = set()

    # Direct match
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)

    # Alias match
    for short, full in ALIASES.items():
        if short in text:
            found_skills.add(full)

    return list(found_skills)