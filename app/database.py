# This file defines the database connection and session management in SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://blog_user:blog_password@localhost:5432/blog")

# Create the engine to connect to Postgres
engine = create_engine(DATABASE_URL)
# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()