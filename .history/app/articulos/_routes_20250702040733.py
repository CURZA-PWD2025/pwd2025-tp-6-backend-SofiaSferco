from flask import Blueprint, request, jsonify
from ._controller import ArticuloController

articulos_bp = Blueprint("articulos", __name__)

@articulos_bp.route("/", methods=["GET"])
def get_all_articulos():
    respuesta, estado = ArticuloController.get_all()
    return jsonify(respuesta), estado

@articulos_bp.route("/<int:id>", methods=["GET"])
def get_articulo(id):
    respuesta, estado = ArticuloController.get_one(id)
    return jsonify(respuesta), estado

@articulos_bp.route("/", methods=["POST"])
def crear_articulo():
    datos = request.get_json()
    respuesta, estado = ArticuloController.create(datos)
    return jsonify(respuesta), estado

@articulos_bp.route("/<int:id>", methods=["PUT"])
def actualizar_articulo(id):
    datos = request.get_json()
    respuesta, estado = ArticuloController.update(id, datos)
    return jsonify(respuesta), estado

@articulos_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_articulo(id):
    respuesta, estado = ArticuloController.delete(id)
    return jsonify(respuesta), estado



