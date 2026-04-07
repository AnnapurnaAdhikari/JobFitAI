def get_skill_gap(user_skills, job):
    user_skills = set([s.lower() for s in user_skills])

    job_skills = set([s.lower() for s in job.get("Skills", [])])
    job_keywords = set([k.lower() for k in job.get("Keywords", [])])

    required = job_skills.union(job_keywords)

    missing = required - user_skills

    return list(missing)