from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Car Price Prediction API",
        "docs": "/docs",
        "health": "/health"
    }