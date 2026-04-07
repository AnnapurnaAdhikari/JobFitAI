import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "data", "skills_database.json")

def flatten_skills():
    with open(FILE_PATH, "r") as f:
        data = json.load(f)

    skills = set()

    for category in data.values():
        for skill in category:
            skills.add(skill.lower())

    return sorted(list(skills))


if __name__ == "__main__":
    skills = flatten_skills()

    output_path = os.path.join(BASE_DIR, "data", "skills_flat.json")

    with open(output_path, "w") as f:
        json.dump(skills, f, indent=4)

    print(f"Total skills: {len(skills)}")