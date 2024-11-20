from sqlalchemy import Column, Integer, Float, String, Date
from app.database import Base

class Specimen(Base):
    __table__name = "specimen"

    id = Column(Integer, primary_key=True, index=True)
    diameter = Column(Integer, index=True)
    height = Column(Integer, index=True)
    test_age_days = Column(Integer, index=True)