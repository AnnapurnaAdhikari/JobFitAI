import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
ROADMAP_PATH = os.path.join(BASE_DIR, "data", "roadmap.json")

def load_roadmap():
    with open(ROADMAP_PATH, "r") as f:
        return json.load(f)

ROADMAP_DB = load_roadmap()["roadmap"]


def generate_roadmap(missing_skills):
    roadmap_output = []

    for skill in missing_skills:
        found = False

        for category in ROADMAP_DB:
            category_name = category["category"]
            skills_list = [s.lower() for s in category["skills"]]

            if skill.lower() in skills_list:
                roadmap_output.append({
                    "skill": skill,
                    "category": category_name,
                    "resources": category["resources"]
                })
                found = True
                break

        # fallback
        if not found:
            roadmap_output.append({
                "skill": skill,
                "category": "General",
                "resources": ["Search online (YouTube, Coursera, etc.)"]
            })

    return roadmap_output