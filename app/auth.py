from datetime import datetime, timedelta
from jose import jwt
from typing import Optional
from sqlalchemy.orm import Session
from os import getenv

from sqlalchemy.sql.functions import user

from app.utils import Utils
from app import models, schemas

SECRET_KEY: str = getenv("SECRET_KEY")
ALGORITHM: str = getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not Utils.verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_username(db: Session, username: str) -> schemas.User:
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip=0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_users(db: Session, user: schemas.UserCreate):
    hashed = Utils.get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        username=user.username,
        full_name=user.full_name,
        hashed_password=hashed,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: schemas.User):

    old_user = (
        db.query(models.User).filter(models.User.username == user.username).first()
    )
    old_user.full_name = user.full_name
    old_user.is_active = user.is_active

    db.commit()
    db.refresh(old_user)
    return old_user


def delete_user(db: Session, user_id: int):
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
