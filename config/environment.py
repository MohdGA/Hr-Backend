import os

db_URI = os.getenv('db_URI')
DATABASE_URL = os.getenv("DATABASE_URL")
secret = os.getenv('SECRET_KEY')

if db_URI and db_URI.startswith("postgres://"):
    db_URI = db_URI.replace("postgres://", "postgresql://", 1)

if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)