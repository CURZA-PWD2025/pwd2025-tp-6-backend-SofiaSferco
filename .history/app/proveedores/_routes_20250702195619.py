from flask import Blueprint, request, jsonify
from ._controller import ProveedorController

proveedores_bp = Blueprint("proveedores", __name__)

@proveedores_bp.route("/", methods=["GET"])
def get_all():
    r, s = ProveedorController.get_all()
    return jsonify(r), s

@proveedores_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    r, s = ProveedorController.get_one(id)
    return jsonify(r), s

@proveedores_bp.route("/", methods=["POST"])
def create():
    r, s = ProveedorController.create(request.get_json())
    return jsonify(r), s

@proveedores_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    r, s = ProveedorController.update(id, request.get_json())
    return jsonify(r), s

@proveedores_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    r, s = ProveedorController.delete(id)
    return jsonify(r), s
