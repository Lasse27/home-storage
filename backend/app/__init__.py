from app.config import Config, DevConfig
from dotenv import load_dotenv
from flask import Flask
from app.setup import AppSetup


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(Config)
    AppSetup.setup_app_directories(app=app)
    AppSetup.setup_extensions(app=app)
    AppSetup.setup_routes(app)
    return app


def create_dev_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    AppSetup.setup_app_directories(app=app)
    AppSetup.setup_extensions(app=app)
    AppSetup.setup_routes(app)
    return app
