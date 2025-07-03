from flask import Blueprint, request, jsonify
from app.articulos._controller import ArticuloController

articulo_bp = Blueprint('articulo_bp', __name__)

@articulo_bp.route('/', methods=['GET'])
def get_articulos():
    result = ArticuloController.get_all()
    return jsonify(result), 200

@articulo_bp.route('/<int:id>', methods=['GET'])
def get_articulo(id):
    result = ArticuloController.get_one(id)
    if result:
        return jsonify(result), 200
    return jsonify({'error': 'Artículo no encontrado'}), 404

@articulo_bp.route('/', methods=['POST'])
def create_articulo():
    data = request.json
    result = ArticuloController.create(data)
    if 'error' in result:
        return jsonify(result), 400
    return jsonify(result), 201

@articulo_bp.route('/<int:id>', methods=['PUT'])
def update_articulo(id):
    data = request.json
    result = ArticuloController.update(id, data)
    if result is None:
        return jsonify({'error': 'Artículo no encontrado'}), 404
    if 'error' in result:
        return jsonify(result), 400
    return jsonify(result), 200

@articulo_bp.route('/<int:id>', methods=['DELETE'])
def delete_articulo(id):
    result = ArticuloController.delete(id)
    if result is None:
        return jsonify({'error': 'Artículo no encontrado'}), 404
    if 'error' in result:
        return jsonify(result), 400
    return jsonify(result), 200


