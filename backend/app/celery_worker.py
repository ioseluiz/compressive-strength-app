from celery import Celery
from app.database import SessionLocal
from app.mixes.mixes import get_mixes
from app.send_email import send_email

celery = Celery(__name__, broker='redis://localhost:6379/0')

@celery.task
def send_daily_emails():
    db = SessionLocal
    mixes_list = get_mixes(db)
    for item in mixes_list:
        send_email("user@example.com", "Mix Date Alert", f"Mix {item.name}.")