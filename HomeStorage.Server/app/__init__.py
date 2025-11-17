from logging import Logger
import logging
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, g, send_from_directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# .env laden
load_dotenv()

LOGGER: Logger
HOME = Path.home()
DEFAULT_FOLDER = Path.joinpath(HOME, "homestorage", "uploads")
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", DEFAULT_FOLDER)


def create_app(dev: bool):
    global LOGGER
    app = Flask(__name__)

    LOGGER = app.logger
    LOGGER.setLevel(logging.DEBUG)
    
    # Create upload folder if it doesn't exist
    if not Path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
        LOGGER.info(f"Created upload folder at: {UPLOAD_FOLDER}")
    LOGGER.info(f"Upload folder set to: {UPLOAD_FOLDER}")

    # Datenbank konfigurieren
    url = get_database_url(dev)
    engine = create_engine(url, echo=True)  # echo=True loggt SQL-Befehle

    # Tabellen erstellen
    from app.models import Base
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # URL-Routen registrieren
    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def serve_vue(path):
        if path != "":
            # Normalize the combined path and ensure it's inside the static folder
            requested_path = os.path.normpath(os.path.join(app.static_folder, path))
            static_folder_abs = os.path.abspath(app.static_folder)
            if requested_path.startswith(static_folder_abs) and os.path.exists(requested_path):
                # Only serve the file if within static folder
                return send_from_directory(app.static_folder, path)
        return send_from_directory(app.static_folder, "index.html")
    
    from app.routes.file_routes import file_bp
    app.register_blueprint(file_bp)

    from app.routes.system_routes import system_bp
    app.register_blueprint(system_bp)
    
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


def get_database_url(dev: bool):
    user = os.getenv("DB_USER", "postgres")
    if user is None:
        LOGGER.warning("DB_USER nicht gesetzt!")

    password = os.getenv("DB_PASSWORD", "password")
    if password is None:
        LOGGER.warning("DB_PASSWORD nicht gesetzt!")

    db_name = os.getenv("DB_NAME", "homestorage_db")
    if db_name is None:
        LOGGER.warning("DB_NAME nicht gesetzt!")
    if not dev:
        return f"postgresql://{user}:{password}@db:5432/{db_name}"
    else:
        return f"postgresql://{user}:{password}@localhost:5432/{db_name}"
