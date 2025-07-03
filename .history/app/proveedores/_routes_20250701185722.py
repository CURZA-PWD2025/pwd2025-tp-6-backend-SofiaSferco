from flask import Blueprint, request, jsonify
from app.proveedores._controller import ProveedorController

proveedor_bp = Blueprint('proveedor_bp', __name__, url_prefix='/proveedores')

@proveedor_bp.route('/', methods=['GET'])
def get_all():
    return jsonify(ProveedorController.get_all())

@proveedor_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    result = ProveedorController.get_one(id)
    if result:
        return jsonify(result)
    return jsonify({'error': 'Proveedor no encontrado'}), 404

@proveedor_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    result = ProveedorController.create(data)
    return jsonify(result), 201

@proveedor_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    result = ProveedorController.update(id, data)
    if result:
        return jsonify(result)
    return jsonify({'error': 'Proveedor no encontrado'}), 404

@proveedor_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    success = ProveedorController.delete(id)
    if success:
        return jsonify({'message': 'Proveedor eliminado'})
    return jsonify({'error': 'Proveedor no encontrado'}), 404

