from flask import Blueprint, request, jsonify
from controllers.articulo_controller import ArticuloController

articulo_bp = Blueprint('articulo_bp', __name__)

@articulo_bp.route('/', methods=['GET'])
def get_all():
    return jsonify(ArticuloController.get_all())

@articulo_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    articulo = ArticuloController.get_one(id)
    if articulo:
        return jsonify(articulo)
    return jsonify({"error": "No encontrado"}), 404

@articulo_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    nuevo = ArticuloController.create(data)
    return jsonify(nuevo), 201

@articulo_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    actualizado = ArticuloController.update(id, data)
    if actualizado:
        return jsonify(actualizado)
    return jsonify({"error": "No encontrado"}), 404

@articulo_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(ArticuloController.delete(id))


