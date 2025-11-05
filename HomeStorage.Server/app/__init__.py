import os
from dotenv import load_dotenv
from flask import Flask, g, logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# .env laden
load_dotenv()


def create_app():

    app = Flask(__name__)

    # Datenbank konfigurieren
    url = get_database_url()
    engine = create_engine(url, echo=True)  # echo=True loggt SQL-Befehle

    # Tabellen erstellen
    from app.models import Base
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # URL-Routen registrieren
    from app.routes.file_routes import file_bp
    app.register_blueprint(file_bp)

    # Session Hooks
    @app.before_request
    def create_session():
        g.db = SessionLocal()

    @app.teardown_request
    def close_session(exception=None):
        db = g.pop("db", None)
        if db:
            db.close()

    return app


def get_database_url():
    user = os.getenv("DB_USER", "postgres")
    if user is None:
        logging.warning("DB_USER nicht gesetzt!")

    password = os.getenv("DB_PASSWORD", "password")
    if password is None:
        logging.warning("DB_PASSWORD nicht gesetzt!")

    db_name = os.getenv("DB_NAME", "homestorage_db")
    if db_name is None:
        logging.warning("DB_NAME nicht gesetzt!")

    return f"postgresql://{user}:{password}@localhost:5432/{db_name}"
