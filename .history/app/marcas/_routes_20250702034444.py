from flask import Blueprint, request, jsonify
from ._controller import MarcaController

marcas_bp = Blueprint("marcas", __name__)

@marcas_bp.route("/", methods=["GET"])
def get_all_marcas():
    respuesta, estado = MarcaController.get_all()
    return jsonify(respuesta), estado

@marcas_bp.route("/<int:id>", methods=["GET"])
def get_marca(id):
    respuesta, estado = MarcaController.get_one(id)
    return jsonify(respuesta), estado

@marcas_bp.route("/", methods=["POST"])
def crear_marca():
    datos = request.get_json()
    respuesta, estado = MarcaController.create(datos)
    return jsonify(respuesta), estado

@marcas_bp.route("/<int:id>", methods=["PUT"])
def actualizar_marca(id):
    datos = request.get_json()
    respuesta, estado = MarcaController.update(id, datos)
    return jsonify(respuesta), estado

@marcas_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_marca(id):
    respuesta, estado = MarcaController.delete(id)
    return jsonify(respuesta), estado
