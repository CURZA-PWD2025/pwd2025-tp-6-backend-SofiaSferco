from .categoria_controller import CategoriaController
from flask import jsonify, request, Blueprint

categoria_bp=Blueprint("categoria", __name__)

@categoria_bp.route("/categorias")
def get_all():
    try:
        categorias = CategoriaController.get_all()
        if categorias:
            return jsonify(categorias), 200
        else:
            return jsonify({"mensaje": "no se encontraron marcas"}),404
    except Exception as e:
        return jsonify({"mensaje":f"error : {str(e)}"}), 500
    
@categoria_bp.route("/categorias/<int:id>")
def get_one(id):
    try:
        categoria = CategoriaController.get_one(id)
        if categoria:
            return jsonify(categoria), 200
        else:
            return jsonify({"mensaje": "no se encontro la marca"}),404
    except Exception as e:
        return jsonify({"mensaje":f"error : {str(e)}"}), 500

@categoria_bp.route("/categorias/", methods=["POST"])
def create():
    try:
        data = request.get_json()
        categorias = CategoriaController.create(data)
        if categorias:
            return jsonify({'mensaje':'marca creada correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al crear el producto"}),404
    except Exception as e:
        return jsonify({"mensaje":f"error : {str(e)}"}), 500

@categoria_bp.route("/categorias/<int:id>", methods=["PUT"])
def modificar(id):
    try:
        data = request.get_json()
        data['id'] = id
        categoria = CategoriaController.update(data)
        if categoria:
            return jsonify({'mensaje':'marca creada correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al crear el producto"}),500
    except Exception as e:
        return jsonify({"mensaje":f"error : {str(e)}"}), 500
    
@categoria_bp.route("/categorias/<int:id>", methods=["DELETE"])
def eliminar(id):
    try:
        categoria = CategoriaController.delete(id)
        if categoria:
            return jsonify({'mensaje':'marca creada correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al crear el producto"}),500
    except Exception as e:
        return jsonify({"mensaje":f"error : {str(e)}"}), 500