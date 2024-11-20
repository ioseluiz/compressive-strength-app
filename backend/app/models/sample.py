from sqlalchemy import Column, Integer, Float, String, Date
from app.database import Base

class Sample(Base):
    __table__name = "sample"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date_taken = Column(Date, index=True)
    invoice = Column(String, index=True)
    truck = Column(String, index=True)
