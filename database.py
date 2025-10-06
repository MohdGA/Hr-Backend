from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from config.environment import db_URI
from models.base import Base

engine = create_engine(
    db_URI
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()