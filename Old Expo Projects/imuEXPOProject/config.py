import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    
    # Database Configuration
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASS = os.getenv("DB_PASS", "")
    DB_NAME = os.getenv("DB_NAME", "expo_leaderboard")
    
    @staticmethod
    def get_db_config():
        return {
            "host": Config.DB_HOST,
            "user": Config.DB_USER,
            "password": Config.DB_PASS,
            "database": Config.DB_NAME
        }
