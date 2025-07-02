from .marca_controller import MarcaController
from flask import jsonify, request, Blueprint

marca_bp=Blueprint("marca", __name__)

@marca_bp.route("/marcas")
def get_all():
    try:
        marcas = MarcaController.get_all()
        if marcas:
            return jsonify(marcas), 200
        else:
            return jsonify({"mensaje": "no se encontraron marcas"}),404
    except Exception as e:
        return jsonify({"mensaje":f"error : {str(e)}"}), 500
    
@marca_bp.route("/marcas/<int:id>")
def get_one(id):
    try:
        marca = MarcaController.get_one(id)
        if marca:
            return jsonify(marca), 200
        else:
            return jsonify({"mensaje": "no se encontro la marca"}),404
    except Exception as e:
        return jsonify({"mensaje":f"error : {str(e)}"}), 500

@marca_bp.route("/marcas/", methods=["POST"])
def create():
    try:
        data = request.get_json()
        marcas = MarcaController.create(data)
        if marcas:
            return jsonify({'mensaje':'marca creada correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al crear el producto"}),404
    except Exception as e:
        return jsonify({"mensaje":f"error : {str(e)}"}), 500

@marca_bp.route("/marcas/<int:id>", methods=["PUT"])
def modificar(id):
    try:
        data = request.get_json()
        data['id'] = id
        marcas = MarcaController.update(data)
        if marcas:
            return jsonify({'mensaje':'marca editada correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al editar la marca"}),500
    except Exception as e:
        return jsonify({"mensaje":f"error : {str(e)}"}), 500
    
@marca_bp.route("/marcas/<int:id>", methods=["DELETE"])
def eliminar(id):
    try:
        marcas = MarcaController.delete(id)
        if marcas:
            return jsonify({'mensaje':'marca eliminada correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al eliminar la marca"}),500
    except Exception as e:
        return jsonify({"mensaje":f"error : {str(e)}"}), 500