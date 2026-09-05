import json
import random
from datetime import date, timedelta


companies = [
    "TechNova Solutions",
    "DataSphere Technologies",
    "CloudWorks India",
    "InnovateX Labs",
    "CodeCraft Systems",
    "NextGen Software",
    "ByteWave Technologies",
    "InnoSoft Solutions",
    "FinTechHub",
    "AIWorks India"
]

locations = [
    "Bangalore",
    "Hyderabad",
    "Pune",
    "Chennai",
    "Mumbai",
    "Delhi",
    "Noida",
    "Gurgaon"
]

job_templates = [
    {
        "title": "Python Backend Developer",
        "skills": ["Python", "FastAPI", "SQL", "Docker", "AWS"],
        "experience": (1, 4),
        "salary": (600000, 1200000),
        "industry": "Software"
    },
    {
        "title": "Backend Developer",
        "skills": ["Python", "Django", "REST API", "PostgreSQL", "Docker"],
        "experience": (2, 5),
        "salary": (700000, 1400000),
        "industry": "Software"
    },
    {
        "title": "Full Stack Developer",
        "skills": ["Python", "React", "JavaScript", "SQL", "Docker"],
        "experience": (2, 5),
        "salary": (700000, 1500000),
        "industry": "Software"
    },
    {
        "title": "Data Scientist",
        "skills": ["Python", "Pandas", "NumPy", "Machine Learning", "SQL"],
        "experience": (1, 4),
        "salary": (700000, 1600000),
        "industry": "Analytics"
    },
    {
        "title": "Data Analyst",
        "skills": ["Python", "SQL", "Excel", "Power BI", "Tableau"],
        "experience": (1, 3),
        "salary": (500000, 1000000),
        "industry": "Analytics"
    },
    {
        "title": "Machine Learning Engineer",
        "skills": ["Python", "Machine Learning", "TensorFlow", "PyTorch", "SQL"],
        "experience": (2, 6),
        "salary": (900000, 1800000),
        "industry": "Artificial Intelligence"
    },
    {
        "title": "AI Engineer",
        "skills": ["Python", "Machine Learning", "LLM", "LangChain", "FastAPI"],
        "experience": (1, 5),
        "salary": (800000, 1800000),
        "industry": "Artificial Intelligence"
    },
    {
        "title": "GenAI Engineer",
        "skills": ["Python", "LLM", "RAG", "LangChain", "Vector Database"],
        "experience": (1, 4),
        "salary": (800000, 1700000),
        "industry": "Artificial Intelligence"
    },
    {
        "title": "DevOps Engineer",
        "skills": ["Docker", "Kubernetes", "AWS", "Jenkins", "Linux"],
        "experience": (2, 6),
        "salary": (800000, 1600000),
        "industry": "Cloud"
    },
    {
        "title": "Cloud Engineer",
        "skills": ["AWS", "Azure", "Docker", "Kubernetes", "Linux"],
        "experience": (2, 6),
        "salary": (800000, 1700000),
        "industry": "Cloud"
    },
    {
        "title": "Java Backend Developer",
        "skills": ["Java", "Spring Boot", "SQL", "Docker", "AWS"],
        "experience": (2, 5),
        "salary": (700000, 1400000),
        "industry": "Software"
    },
    {
        "title": "Frontend Developer",
        "skills": ["JavaScript", "React", "HTML", "CSS", "TypeScript"],
        "experience": (1, 4),
        "salary": (500000, 1200000),
        "industry": "Software"
    }
]

jobs = []


# Guaranteed jobs for testing the AI Agent
guaranteed_jobs = [
    {
        "id": 1,
        "title": "Python Backend Developer",
        "company": "TechNova Solutions",
        "location": "Bangalore",
        "employment_type": "Full-time",
        "experience_min": 2,
        "experience_max": 4,
        "salary_min": 700000,
        "salary_max": 1100000,
        "skills": ["Python", "FastAPI", "SQL", "Docker", "AWS"],
        "remote": True,
        "education": "Bachelor's degree",
        "industry": "Software",
        "description": "Develop and maintain scalable backend APIs.",
        "posted_date": "2026-09-01"
    },
    {
        "id": 2,
        "title": "Backend Developer",
        "company": "DataSphere Technologies",
        "location": "Bangalore",
        "employment_type": "Full-time",
        "experience_min": 1,
        "experience_max": 3,
        "salary_min": 650000,
        "salary_max": 1000000,
        "skills": ["Python", "Django", "SQL", "Docker"],
        "remote": True,
        "education": "Bachelor's degree",
        "industry": "Software",
        "description": "Build and maintain backend services and REST APIs.",
        "posted_date": "2026-09-02"
    },
    {
        "id": 3,
        "title": "Python Developer",
        "company": "CloudWorks India",
        "location": "Bangalore",
        "employment_type": "Full-time",
        "experience_min": 2,
        "experience_max": 5,
        "salary_min": 800000,
        "salary_max": 1300000,
        "skills": ["Python", "FastAPI", "PostgreSQL", "AWS"],
        "remote": False,
        "education": "Bachelor's degree",
        "industry": "Cloud",
        "description": "Develop Python applications and cloud-based services.",
        "posted_date": "2026-09-03"
    },
    {
        "id": 4,
        "title": "FastAPI Backend Engineer",
        "company": "InnovateX Labs",
        "location": "Bangalore",
        "employment_type": "Full-time",
        "experience_min": 2,
        "experience_max": 4,
        "salary_min": 750000,
        "salary_max": 1200000,
        "skills": ["Python", "FastAPI", "SQL", "Docker", "Redis"],
        "remote": True,
        "education": "Bachelor's degree",
        "industry": "Software",
        "description": "Develop high-performance backend APIs using FastAPI.",
        "posted_date": "2026-09-03"
    },
    {
        "id": 5,
        "title": "Python Backend Engineer",
        "company": "AIWorks India",
        "location": "Remote",
        "employment_type": "Full-time",
        "experience_min": 2,
        "experience_max": 5,
        "salary_min": 850000,
        "salary_max": 1400000,
        "skills": ["Python", "FastAPI", "SQL", "Docker", "Kubernetes"],
        "remote": True,
        "education": "Bachelor's degree",
        "industry": "Artificial Intelligence",
        "description": "Build scalable Python backend services for AI applications.",
        "posted_date": "2026-09-04"
    }
]


# Add the guaranteed jobs first
jobs.extend(guaranteed_jobs)


# Generate the remaining 45 jobs
for job_id in range(6, 51):

    template = random.choice(job_templates)

    min_exp, max_exp = template["experience"]
    min_salary, max_salary = template["salary"]

    job = {
        "id": job_id,
        "title": template["title"],
        "company": random.choice(companies),
        "location": random.choice(locations),
        "employment_type": random.choice(
            ["Full-time", "Full-time", "Contract"]
        ),
        "experience_min": min_exp,
        "experience_max": max_exp,
        "salary_min": min_salary,
        "salary_max": max_salary,
        "skills": template["skills"],
        "remote": random.choice([True, False]),
        "education": "Bachelor's degree",
        "industry": template["industry"],
        "description": (
            f"Work as a {template['title']} and contribute to "
            "building scalable and reliable technology solutions."
        ),
        "posted_date": (
            date.today() - timedelta(days=random.randint(0, 30))
        ).isoformat()
    }

    jobs.append(job)


# Save all jobs to jobs.json
with open("jobs.json", "w", encoding="utf-8") as file:
    json.dump(jobs, file, indent=2)


print(f"Successfully generated {len(jobs)} jobs.")
