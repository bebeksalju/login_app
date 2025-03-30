from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt, JWTError

from app.config import settings
from app.database import SessionLocal
from app.models.User import User
from app.schemas.user import UserCreate, UserResponse
from app.repositories.user_repository import create_user, get_user_by_username
from app.repositories.token_blacklist import add_token_to_blacklist
from app.services.auth_service import login_user
from app.utils.security import (
    verify_password,
    create_access_token,
    create_refresh_token,
    get_current_user
    )

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username sudah terdaftar!")
    return create_user(db, user)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    access_token = create_access_token({
        "sub": user.username
    })
    refresh_token = create_refresh_token({
        "sub":user.username
    })
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token-type":"bearer"
    }

@router.post("/refresh")
def refresh_access_token(refresh_token: str):
    try:
        payload = jwt.decode(
            refresh_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    
    new_access_token = create_access_token({
        "sub":username
    })
    return {
        "access_token": new_access_token,
        "token-type":"bearer"
    }
    
@router.post("/logout")
def logout(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    add_token_to_blacklist(db, current_user["token"])
    return {"message": "Logout successful"}
