import json

from apscheduler.schedulers.background import BackgroundScheduler

from app.vector_store import add_knowledge_to_vector_db


# -----------------------------------
# FILE PATH
# -----------------------------------

DATA_FILE = "data/knowledge.json"


# -----------------------------------
# SYNCHRONIZE KNOWLEDGE WITH CHROMADB
# -----------------------------------

def sync_knowledge_to_vector_db():

    print("Starting knowledge synchronization...")


    with open(DATA_FILE, "r") as file:

        knowledge_base = json.load(file)


    for knowledge in knowledge_base:

        add_knowledge_to_vector_db(

            knowledge_id=knowledge["id"],

            category=knowledge["category"],

            content=knowledge["content"]

        )


    print("Knowledge synchronization completed!")


# -----------------------------------
# CREATE SCHEDULER
# -----------------------------------

scheduler = BackgroundScheduler()


# -----------------------------------
# START SCHEDULER
# -----------------------------------

def start_scheduler(interval_minutes: int = 1):

    # Check if scheduler is already running

    if scheduler.running:

        return False


    # Add synchronization job

    scheduler.add_job(

        sync_knowledge_to_vector_db,

        trigger="interval",

        minutes=interval_minutes,

        id="knowledge_sync_job",

        replace_existing=True

    )


    # Start scheduler

    scheduler.start()


    print(
        f"Scheduler started successfully! "
        f"Running every {interval_minutes} minute(s)."
    )


    return True