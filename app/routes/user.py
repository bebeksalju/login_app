from fastapi import APIRouter, Depends
from app.utils.security import get_current_user

router = APIRouter()

@router.get("/profile")
def get_profile(current_user: str = Depends(get_current_user)):
    return {
        "message": "Welcome!",
        "username":current_user
    }