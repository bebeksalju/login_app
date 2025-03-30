from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
import datetime

class TokenBlackList(Base):
    __tablename__ = "token_blacklist"
    
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)