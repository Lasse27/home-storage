"""
/ File Management Endpoints
----------------------------
/ GET    /files/                    -> Get multiple file metadata
/ GET    /files/<file_id>           -> Get single file metadata by ID
/ PATCH  /files/<file_id>           -> Update file metadata by ID
/ DELETE /files/<file_id>           -> Delete file by ID
/ POST   /files/upload              -> Upload a new file
/ GET    /files/download/<file_id>  -> Download a file by ID
"""

from flask import Blueprint, request, jsonify, g
from app.repositories import FileRepository
from app.services.file_service import FileService
from app.services.exceptions import ServiceException


file_bp = Blueprint("file_bp", __name__, url_prefix="/files")


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
        return jsonify({"error": service_e.message, "meta": service_e.meta}), service_e.status

    except Exception as e:
        return jsonify({"error": "Unhandled server error", "meta": str(e)}), 500


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
        return jsonify({"error": service_e.message, "meta": service_e.meta}), service_e.status

    except Exception as e:
        return jsonify({"error": "Unhandled server error", "meta": str(e)}), 500


# # Updates metadata of a specific file by ID
# @file_bp.route("/<string:file_id>", methods=["PATCH"])
# def update_file_meta(file_id):
#     return jsonify({"message": f"Update file metadata for file ID: {file_id}"}), 200


# # Deletes a specific file by ID
# @file_bp.route("/<string:file_id>", methods=["DELETE"])
# def delete_file(file_id):
#     return jsonify({"message": f"Delete file with ID: {file_id}"}), 200


# # Uploads a new file
# @file_bp.route("/upload", methods=["POST"])
# def upload_file():
#     return jsonify({"message": "Upload new file"}), 201


# # Downloads a specific file by ID
# @file_bp.route("/download/<string:file_id>", methods=["GET"])
# def download_single_file(file_id):
#     return jsonify({"message": f"Download file with ID: {file_id}"}), 200
