"""Konfigurasi aplikasi yang dibaca dari file .env."""

import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "raincode-development-key")
    DEBUG = os.getenv("APP_DEBUG", "True").lower() == "true"

    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
    DB_PORT = int(os.getenv("DB_PORT", "3306"))
    DB_USER = os.getenv("DB_USER", "expense_app")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_NAME = os.getenv("DB_NAME", "expense_tracker")

    RECENT_EXPENSES_LIMIT = int(os.getenv("RECENT_EXPENSES_LIMIT", "5"))


config = Config()
