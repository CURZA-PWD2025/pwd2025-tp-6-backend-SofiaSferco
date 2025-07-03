from flask import Blueprint, request, jsonify
from app.marcas._controller import MarcaController

marca_bp = Blueprint('marca_bp', __name__)

@marca_bp.route('/', methods=['GET'])
def get_all():
    return jsonify(MarcaController.get_all())

@marca_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    result = MarcaController.get_one(id)
    if result:
        return jsonify(result)
    return jsonify({'error': 'Marca no encontrada'}), 404

@marca_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    result = MarcaController.create(data)
    return jsonify(result), 201

@marca_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    result = MarcaController.update(id, data)
    if result:
        return jsonify(result)
    return jsonify({'error': 'Marca no encontrada'}), 404

@marca_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    success = MarcaController.delete(id)
    if success:
        return jsonify({'message': 'Marca eliminada'})
    return jsonify({'error': 'Marca no encontrada'}), 404
