import os
from pathlib import Path
from flask import Flask


class AppSetup:
    def __init__(self):
        pass

    @staticmethod
    def setup_app_directories(app: Flask):
        uploadFolder = app.config["UPLOAD_FOLDER"]
        if not Path.exists(uploadFolder):
            os.makedirs(uploadFolder)
            app.logger.info(f"Created upload folder at: {uploadFolder}")
        app.logger.info(f"Upload folder set to: {uploadFolder}")

    @staticmethod
    def setup_extensions(app: Flask):
        from app.extensions import db, migrate

        db.init_app(app)
        migrate.init_app(app, db)

    @staticmethod
    def setup_routes(app: Flask):
        from app.routes.file_routes import file_bp
        from app.routes.system_routes import system_bp

        app.register_blueprint(file_bp)
        app.register_blueprint(system_bp)
