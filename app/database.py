from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from sqlalchemy.orm import sessionmaker

DB_URL = getenv("DATABASE_URL")

# Fix needed as heroku returns DB starting with postgres://
if DB_URL.startswith("postgres://"):
    DB_URL = DB_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
