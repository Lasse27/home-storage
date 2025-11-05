"""
/ File Management Endpoints
----------------------------
/ GET    /files/                    -> Get multiple file metadata
/ GET    /files/<file_id>           -> Get single file metadata by ID
/ PATCH  /files/<file_id>           -> Update file metadata by ID
/ PATCH  /files/<file_id>           -> Delete file by ID
/ POST   /files/upload              -> Upload a new file
/ GET    /files/download/<file_id>  -> Download a file by ID
"""

from flask import Blueprint, request, jsonify, g

file_bp = Blueprint("file_bp", __name__, url_prefix="/files")


# Gets a list of file informations (paging, filtering, etc. )
@file_bp.route("/", methods=["GET"])
def get_multi_file_meta():
    return jsonify({"message": "Get multiple file metadata"}), 200


# Gets a specific file information by ID
@file_bp.route("/<string:file_id>", methods=["GET"])
def get_single_file_meta(file_id):
    return jsonify({"message": f"Get file metadata for file ID: {file_id}"}), 200


# Updates metadata of a specific file by ID
@file_bp.route("/<string:file_id>", methods=["PATCH"])
def update_file_meta(file_id):
    return jsonify({"message": f"Update file metadata for file ID: {file_id}"}), 200


# Deletes a specific file by ID
@file_bp.route("/<string:file_id>", methods=["PATCH"])
def delete_file(file_id):
    return jsonify({"message": f"Delete file with ID: {file_id}"}), 200


# Uploads a new file
@file_bp.route("/upload", methods=["POST"])
def upload_file():
    return jsonify({"message": "Upload new file"}), 201


# Downloads a specific file by ID
@file_bp.route("/download/<string:file_id>", methods=["GET"])
def download_single_file(file_id):
    return jsonify({"message": f"Download file with ID: {file_id}"}), 200
