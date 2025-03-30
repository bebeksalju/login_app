from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.user_repository import get_user_by_username
from app.utils.security import verify_password, create_access_token
from datetime import timedelta

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return user

def login_user(db: Session, username: str, password: str):
    user = authenticate_user(db, username, password)
    access_token = create_access_token(
        data={
            "sub":user.username
        }, expires_delta=timedelta(hours=1)
    )
    return {
        "access_token":access_token,
        "token-type":"bearer"
    }