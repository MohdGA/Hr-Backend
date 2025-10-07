from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from config.environment import DATABASE_URL
from models.base import Base

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()