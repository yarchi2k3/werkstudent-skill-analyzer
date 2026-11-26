from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    location = Column(String)
    description = Column(String, nullable=False)
    employment_type = Column(String)
    source_url = Column(String)
    publication_date = Column(Date)
    collected_at = Column(DateTime, default=datetime.utcnow)
    
engine = create_engine("sqlite:///data/jobs.db")
Base.metadata.create_all(engine)