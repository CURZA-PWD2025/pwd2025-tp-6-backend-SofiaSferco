
from flask import Blueprint, request, jsonify
from app.categorias._controller import CategoriaController

categoria_bp = Blueprint('categoria_bp', __name__, url_prefix='/categorias')

@categoria_bp.route('/', methods=['GET'])
def get_all():
    return jsonify(CategoriaController.get_all())

@categoria_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    result = CategoriaController.get_one(id)
    if result:
        return jsonify(result)
    return jsonify({'error': 'Categoría no encontrada'}), 404

@categoria_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    result = CategoriaController.create(data)
    return jsonify(result), 201

@categoria_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    result = CategoriaController.update(id, data)
    if result:
        return jsonify(result)
    return jsonify({'error': 'Categoría no encontrada'}), 404

@categoria_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    success = CategoriaController.delete(id)
    if success:
        return jsonify({'message': 'Categoría eliminada'})
    return jsonify({'error': 'Categoría no encontrada'}), 404
