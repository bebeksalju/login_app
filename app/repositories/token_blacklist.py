from sqlalchemy.orm import Session
from app.models.token_blacklist import TokenBlackList

def add_token_to_blacklist(db: Session, token: str):
    db_token = TokenBlackList(token=token)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token

def is_token_blacklisted(db: Session, token: str) -> bool:
    return db.query(TokenBlackList).filter(TokenBlackList.token == token).first() is not None