from .articulo_controller import ArticulosController
from .articulo_model import ArticuloModel
from flask import jsonify, request, Blueprint, Response, make_response
import json

articulos_bp = Blueprint("articulos", __name__)

# este codigo daba el json pero desordenado, es como lo enseño el profesor


@articulos_bp.route("/articulos", methods=["GET"])
def get_all():
    try:
        categorias = ArticulosController.get_all()
        if categorias:
            return jsonify(categorias), 200
        else:
            return jsonify({"mensaje": "no se encontraron marcas"}),404
    except Exception as e:
        return jsonify({"mensaje":f"error : {str(e)}"}), 500


@articulos_bp.route("/articulos/<int:id>")
def get_one(id):
    try:
        categoria = ArticulosController.get_one(id)
        if categoria:
            return jsonify(categoria), 200
        else:
            return jsonify({"mensaje": "no se encontro la marca"}),404
    except Exception as e:
        return jsonify({"mensaje":f"error : {str(e)}"}), 500


@articulos_bp.route("/articulos/", methods=["POST"])
def create():
    try:
        data = request.get_json()
        categorias = ArticulosController.create(data)
        if categorias:
            return jsonify({'mensaje':'articulo creado correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al crear el producto"}),404
    except Exception as e:
        return jsonify({"mensaje":f"error : {str(e)}"}), 500

@articulos_bp.route('/articulos/<int:id>', methods=['PUT'])
def update(id):
    try:
        data = request.get_json()
        data['id'] = id
        articulo = ArticulosController.update(data)
        if articulo:
            return jsonify({'mensaje': 'articulo modificado con exito'}), 201
        else:
            return jsonify({'mensaje': 'articulo no encontrado'}), 404
    except Exception as e:
        return jsonify({'mensaje' : f'error al modificar articulo {e}'}), 500

@articulos_bp.route('/articulos/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        articulo= ArticulosController.delete(id)
        if articulo:
            return jsonify({'mensaje': 'Articulo eliminado con exito'}), 201
        else:
            return jsonify({'mensaje':'Articulo no encontrado'}), 404
    except Exception as e:
        return jsonify({'mensaje': f'error al quere borrar articulo {e}'}), 500