from sqlalchemy import Column, Integer, String, DateTime

from app.database import Base


class IncidentEntry(Base):
    __tablename__ = "Mass_Shooting_Incidents"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    killed = Column(Integer, nullable=False)
    wounded = Column(Integer, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    names = Column(String, nullable=False)
    sources = Column(String, nullable=False)
    suspect_status = Column(String, nullable=False)
    suspect_keyword = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
