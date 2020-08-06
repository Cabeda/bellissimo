from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from sqlalchemy.orm import sessionmaker
 
SQLALCHEMY_DATABASE_URL = getenv("DB_CONN")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)

Base = declarative_base()