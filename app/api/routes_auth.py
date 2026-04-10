import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.security import create_token

router = APIRouter()

AUTH_USERNAME = os.getenv("AUTH_USERNAME")
AUTH_PASSWORD = os.getenv("AUTH_PASSWORD")


class AuthInput(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(auth: AuthInput):
    if auth.username == AUTH_USERNAME and auth.password == AUTH_PASSWORD:
        token = create_token({"sub": auth.username})
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid Credentials!")