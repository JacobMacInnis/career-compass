from dotenv import load_dotenv
load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

if os.getenv("K_SERVICE"):
    DATABASE_URL = os.getenv("CLOUD_DATABASE_URL")
else: 
    DATABASE_URL = os.getenv("LOCAL_DATABASE_URL")

if not DATABASE_URL:
    raise Exception("DATABASE_URL environment variable is not set.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_db_and_tables():
    from src.db.models import Base
    Base.metadata.create_all(bind=engine)
