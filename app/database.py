from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

engine = create_engine("sqlite:///Mass_Shooting_Data.db", echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)
