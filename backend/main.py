from fastapi import FastAPI
from app.database import engine, Base
from app.celery_worker import send_daily_emails
from datetime import datetime, date, time
from app import routes
from app import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.auth.router)
app.include_router(routes.mixes.router)

# Schedule the daily mix task
send_daily_emails.apply_async(eta=datetime.combine(date.today(), time(12,0)))