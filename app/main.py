from fastapi import FastAPI

from app.routes import auth, user
from app.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(auth.router, prefix="/auth")
app.include_router(user.router, prefix="/users")