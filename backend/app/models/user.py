from sqlalchemy import Column, Integer, Float, String, Date
from app.database import Base

class User(Base):
    username = Column(String, index=True)