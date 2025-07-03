from flask import Blueprint, request, jsonify
from ._controller import CategoriaController

categorias_bp = Blueprint("categorias", __name__)

@categorias_bp.route("/", methods=["GET"])
def get_all_categorias():
    respuesta, estado = CategoriaController.get_all()
    return jsonify(respuesta), estado

@categorias_bp.route("/<int:id>", methods=["GET"])
def get_categoria(id):
    respuesta, estado = CategoriaController.get_one(id)
    return jsonify(respuesta), estado

@categorias_bp.route("/", methods=["POST"])
def crear_categoria():
    datos = request.get_json()
    respuesta, estado = CategoriaController.create(datos)
    return jsonify(respuesta), estado

@categorias_bp.route("/<int:id>", methods=["PUT"])
def actualizar_categoria(id):
    datos = request.get_json()
    respuesta, estado = CategoriaController.update(id, datos)
    return jsonify(respuesta), estado

@categorias_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_categoria(id):
    respuesta, estado = CategoriaController.delete(id)
    return jsonify(respuesta), estado
