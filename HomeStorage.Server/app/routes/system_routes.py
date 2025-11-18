"""
/ System Info Routes
----------------------------
/ GET   /api/system         -> Return full info for executing system (same as calling each other endpoint)
/ GET   /api/system/cpu     -> Return CPU info for executing system
/ GET   /api/system/disk    -> Return disk info for executing system
/ GET   /api/system/memory  -> Return memory info for executing system
"""
import traceback
from flask import Blueprint, current_app, jsonify
from app.services.exceptions import ServiceException
from app.services.system_service import SystemService
from app.dtos.system_response import *

system_bp: Blueprint = Blueprint(
    "system_bp", __name__, url_prefix="/api/system")


@system_bp.get("/")
def system_full():
    try:
        service: SystemService = SystemService()
        info: SystemCpuResponse = service.get_full_system_info()
        return jsonify(info.model_dump()), 200

    except ServiceException as service_e:
        return jsonify({"error": service_e.message, "meta": service_e.meta}), service_e.status

    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        return jsonify({"error": "Unhandled server error"}), 500


@system_bp.get("/cpu")
def system_cpu():
    try:
        service: SystemService = SystemService()
        info: SystemCpuResponse = service.get_cpu_info()
        return jsonify(info.model_dump()), 200

    except ServiceException as service_e:
        return jsonify({"error": service_e.message, "meta": service_e.meta}), service_e.status

    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        return jsonify({"error": "Unhandled server error"}), 500


@system_bp.get("/disk")
def system_disk():
    try:
        service: SystemService = SystemService()
        info: SystemDiskResponse = service.get_disk_info()
        return jsonify(info.model_dump()), 200

    except ServiceException as service_e:
        return jsonify({"error": service_e.message, "meta": service_e.meta}), service_e.status

    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        return jsonify({"error": "Unhandled server error"}), 500


@system_bp.get("/memory")
def system_memory():
    try:
        service: SystemService = SystemService()
        info: SystemMemoryResponse = service.get_memory_info()
        return jsonify(info.model_dump()), 200

    except ServiceException as service_e:
        return jsonify({"error": service_e.message, "meta": service_e.meta}), service_e.status

    except Exception as e:
        current_app.logger.error(traceback.format_exc())
        return jsonify({"error": "Unhandled server error"}), 500
