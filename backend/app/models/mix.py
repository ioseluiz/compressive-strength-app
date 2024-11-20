from sqlalchemy import Column, Integer, Float, String, Date
from app.database import Base

class Sample(Base):
    __table__name = "sample"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    compressive_strength = Column(Integer, index=True)
    design_age = Column(Integer, index=True)