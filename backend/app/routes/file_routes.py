import traceback
from flask import Blueprint, current_app, request, jsonify, g
from app.repositories import FileRepository
from app.services.file_service import FileService
from app.services.exceptions import ServiceException

file_bp: Blueprint = Blueprint("file_bp", __name__, url_prefix="/api/files")


@file_bp.route("/", methods=["GET"])
def read_multiple_files():
    """Gets metadata for multiple files with pagination."""
    try:
        # Get query parameters
        start: int = request.args.get("start", default=0, type=int)
        limit: int = request.args.get("limit", default=100, type=int)

        # Initialize repository and service
        repository = FileRepository(g.db)
        service = FileService(repository)

        # Call service method
        files = service.read_files(offset=start, limit=limit)
        return jsonify(files), 200

    except ServiceException as service_e:
        response = {"error": service_e.message, "meta": service_e.meta}
        return jsonify(response), service_e.status

    except Exception:
        current_app.logger.error(traceback.format_exc())
        return jsonify({"error": "Unhandled server error"}), 500


@file_bp.route("/<string:file_id>", methods=["GET"])
def read_single_file(file_id: str):
    try:
        # Initialize repository and service
        repository = FileRepository(g.db)
        service = FileService(repository)

        # Call service method
        files = service.read_file_by_id(file_id)
        return jsonify(files), 200

    except ServiceException as service_e:
        response = {"error": service_e.message, "meta": service_e.meta}
        return jsonify(response), service_e.status

    except Exception:
        current_app.logger.error(traceback.format_exc())
        return jsonify({"error": "Unhandled server error"}), 500


# Uploads a new file
@file_bp.route("/upload", methods=["POST"])
def upload_file():
    pass
