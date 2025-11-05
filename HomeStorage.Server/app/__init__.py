import os
from dotenv import load_dotenv
from flask import Flask, g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# .env laden
load_dotenv()

def create_app():
    app = Flask(__name__)

    DATABASE_URL = os.getenv("DATABASE_URL")
    if DATABASE_URL is None:
        raise ValueError("DATABASE_URL nicht gesetzt!")
    
    engine = create_engine(DATABASE_URL, echo=True)  # echo=True loggt SQL-Befehle
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Session pro Request erzeugen
    @app.before_request
    def create_session():
        g.db = SessionLocal()

    # Session schließen
    @app.teardown_request
    def close_session(exception=None):
        db = g.pop("db", None)
        if db:
            db.close()

    return app
