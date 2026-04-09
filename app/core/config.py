import os
from dotenv import load_dotenv

load_dotenv()


class Settings():
    PROJECT_NAME="Car Price Prediction API"
    API_KEY=os.getenv("API_KEY")
    JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM="HS256"
    REDIS_URL=os.getenv("REDIS_URL")
    MODEL_PATH="app/models/model.joblib"


settings = Settings()