import os
from pathlib import Path
from flask import current_app


def get_database_url():
    user = os.getenv("POSTGRES_USER")
    if user is None:
        current_app.logger.warning("POSTGRES_USER nicht gesetzt!")
        user = "postgres"

    password = os.getenv("POSTGRES_PASSWORD")
    if password is None:
        current_app.logger.warning("POSTGRES_PASSWORD nicht gesetzt!")
        password = "password"

    db_name = os.getenv("POSTGRES_DB")
    if db_name is None:
        current_app.logger.warning("POSTGRES_DB nicht gesetzt!")
        db_name = "homestorage_db"

    return f"postgresql://{user}:{password}@postgres:5432/{db_name}"


class Config:
    # File Uploads
    DEFAULT_FOLDER = Path.joinpath(Path.home(), "homestorage", "uploads")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", DEFAULT_FOLDER)

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = get_database_url()
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # empfohlen


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
