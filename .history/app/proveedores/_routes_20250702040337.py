from flask import Blueprint, request, jsonify
from ._controller import ProveedorController

proveedores_bp = Blueprint("proveedores", __name__)

@proveedores_bp.route("/", methods=["GET"])
def get_all_proveedores():
    respuesta, estado = ProveedorController.get_all()
    return jsonify(respuesta), estado

@proveedores_bp.route("/<int:id>", methods=["GET"])
def get_proveedor(id):
    respuesta, estado = ProveedorController.get_one(id)
    return jsonify(respuesta), estado

@proveedores_bp.route("/", methods=["POST"])
def crear_proveedor():
    datos = request.get_json()
    respuesta, estado = ProveedorController.create(datos)
    return jsonify(respuesta), estado

@proveedores_bp.route("/<int:id>", methods=["PUT"])
def actualizar_proveedor(id):
    datos = request.get_json()
    respuesta, estado = ProveedorController.update(id, datos)
    return jsonify(respuesta), estado

@proveedores_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_proveedor(id):
    respuesta, estado = ProveedorController.delete(id)
    return jsonify(respuesta), estado
