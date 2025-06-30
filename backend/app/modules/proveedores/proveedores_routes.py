from .proveedores_controller import ProveedoresController
from flask import jsonify, request, Blueprint, Response, make_response
import json

proveedores_bp=Blueprint("proveedores", __name__)

#este codigo daba el json pero desordenado, es como lo enseño el profesor
# @proveedores_bp.route("/proveedores")
# def get_all():
#     try:
#         proveedores = ProveedoresController.get_all()
#         if proveedores:
#             return jsonify(proveedores), 200
#         else:
#             return jsonify({"mensaje": "no se encontraron marcas"}),404
#     except Exception as e:
#         return jsonify({"mensaje":f"error : {str(e)}"}), 500
    
@proveedores_bp.route("/proveedores")
def get_all():
    try:
        proveedores = ProveedoresController.get_all()
        if proveedores:
            data = []
            for p in proveedores:
                item = {
                    'id': p['id'],
                    'nombre': p['nombre'],
                    'email': p['email'],
                    'telefono': p['telefono'],
                    'direccion': p['direccion']
                }
                data.append(item)
            response = make_response(json.dumps(data, ensure_ascii=False), 200)
            response.headers["Content-Type"] = "application/json" #le dice al navegador que se esta enviando un texto
            return response
        else:
            return jsonify({"mensaje": "no se encontraron proveedores"}), 404
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500    




@proveedores_bp.route("/proveedores/<int:id>")
def get_one(id):
    try:
        categoria = ProveedoresController.get_one(id)
        if categoria:
            return jsonify(categoria), 200
        else:
            return jsonify({"mensaje": "no se encontro la marca"}),404
    except Exception as e:
        return jsonify({"mensaje":f"error : {str(e)}"}), 500

@proveedores_bp.route("/proveedores/", methods=["POST"])
def create():
    try:
        data = request.get_json()
        categorias = ProveedoresController.create(data)
        if categorias:
            return jsonify({'mensaje':'marca creada correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al crear el producto"}),404
    except Exception as e:
        return jsonify({"mensaje":f"error : {str(e)}"}), 500

@proveedores_bp.route("/proveedores/<int:id>", methods=["PUT"])
def modificar(id):
    try:
        data = request.get_json()
        data['id'] = id
        categoria = ProveedoresController.update(data)
        if categoria:
            return jsonify({'mensaje':'marca creada correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al crear el producto"}),500
    except Exception as e:
        return jsonify({"mensaje":f"error : {str(e)}"}), 500
    
@proveedores_bp.route("/proveedores/<int:id>", methods=["DELETE"])
def eliminar(id):
    try:
        categoria = ProveedoresController.delete(id)
        if categoria:
            return jsonify({'mensaje':'marca creada correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al crear el producto"}),500
    except Exception as e:
        return jsonify({"mensaje":f"error : {str(e)}"}), 500