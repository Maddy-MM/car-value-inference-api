import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME = "Car Price Prediction API"

    # Auth credentials 
    AUTH_USERNAME = os.getenv("AUTH_USERNAME")
    AUTH_PASSWORD = os.getenv("AUTH_PASSWORD")

    # Configs
    API_KEY = os.getenv("API_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM = "HS256"
    REDIS_URL = os.getenv("REDIS_URL")

    # Paths
    MODEL_PATH = "app/models/model.joblib"


settings = Settings()