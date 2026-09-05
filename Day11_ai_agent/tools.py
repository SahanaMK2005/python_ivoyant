import json


def search_jobs(
    title: str = "",
    location: str = "",
    skills: list[str] | None = None,
    remote: bool = False
):
    """
    Search jobs from the local jobs.json dataset.

    The search is flexible:
    - title keywords are matched against the job title
    - location is matched against the job location
    - skills are matched against the job's skills
    - remote filters remote jobs
    """

    with open("jobs.json", "r", encoding="utf-8") as file:
        jobs = json.load(file)

    matches = []

    # Convert title into individual keywords
    title_keywords = title.lower().split() if title else []

    for job in jobs:

        # ------------------------------------------------
        # 1. Title matching
        # ------------------------------------------------
        if title_keywords:
            job_title = job["title"].lower()

            title_match = any(
                keyword in job_title
                for keyword in title_keywords
            )

            if not title_match:
                continue

        # ------------------------------------------------
        # 2. Location matching
        # ------------------------------------------------
        if location:
            if location.lower() != job["location"].lower():
                continue

        # ------------------------------------------------
        # 3. Remote matching
        # ------------------------------------------------
        if remote and not job["remote"]:
            continue

        # ------------------------------------------------
        # 4. Skills matching
        # ------------------------------------------------
        if skills:

            job_skills = {
                skill.lower()
                for skill in job["skills"]
            }

            requested_skills = {
                skill.lower()
                for skill in skills
            }

            # At least one requested skill should match
            if not requested_skills.intersection(job_skills):
                continue

        matches.append(job)

    return matches

def analyze_job_suitability(
    job: dict,
    experience: int,
    skills: list[str],
    expected_salary: int,
    remote_preference: bool = False
):
    """
    Analyze how suitable a job is for a candidate.
    """

    score = 0
    reasons = []
    missing_skills = []

    # 1. Experience check
    if job["experience_min"] <= experience <= job["experience_max"]:
        score += 25
        reasons.append("Experience matches the job requirement.")
    elif experience >= job["experience_min"]:
        score += 15
        reasons.append("Experience is close to the required range.")
    else:
        reasons.append("Candidate does not meet the minimum experience requirement.")

    # 2. Skills check
    candidate_skills = {skill.lower() for skill in skills}
    job_skills = {skill.lower() for skill in job["skills"]}

    matching_skills = candidate_skills.intersection(job_skills)
    missing_skills = job_skills - candidate_skills

    if job_skills:
        skill_score = (len(matching_skills) / len(job_skills)) * 40
        score += skill_score

    if matching_skills:
        reasons.append(
            f"Matching skills: {', '.join(sorted(matching_skills))}."
        )

    if missing_skills:
        reasons.append(
            f"Missing skills: {', '.join(sorted(missing_skills))}."
        )

    # 3. Salary check
    if job["salary_min"] <= expected_salary <= job["salary_max"]:
        score += 20
        reasons.append("Expected salary is within the job's salary range.")
    else:
        reasons.append("Expected salary is outside the job's salary range.")

    # 4. Remote preference
    if remote_preference:
        if job["remote"]:
            score += 15
            reasons.append("Remote work is available.")
        else:
            reasons.append("Remote work is not available.")

    return {
        "job_id": job["id"],
        "job_title": job["title"],
        "company": job["company"],
        "match_score": round(score, 2),
        "matching_skills": sorted(matching_skills),
        "missing_skills": sorted(missing_skills),
        "reasons": reasons
    }

if __name__ == "__main__":

    results = search_jobs(
        title="Python Backend Developer",
        location="Bangalore",
        remote=True
    )

    print("Matching jobs:", len(results))

    for job in results:
        print(
            job["id"],
            "|",
            job["title"],
            "|",
            job["company"],
            "| Remote:",
            job["remote"]
        )