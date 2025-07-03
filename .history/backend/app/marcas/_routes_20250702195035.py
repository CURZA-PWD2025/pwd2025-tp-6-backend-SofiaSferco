from flask import Blueprint, request, jsonify
from ._controller import MarcaController

marcas_bp = Blueprint("marcas", __name__)

@marcas_bp.route("/", methods=["GET"])
def get_all():
    r, s = MarcaController.get_all()
    return jsonify(r), s

@marcas_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    r, s = MarcaController.get_one(id)
    return jsonify(r), s

@marcas_bp.route("/", methods=["POST"])
def create():
    r, s = MarcaController.create(request.get_json())
    return jsonify(r), s

@marcas_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    r, s = MarcaController.update(id, request.get_json())
    return jsonify(r), s

@marcas_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    r, s = MarcaController.delete(id)
    return jsonify(r), s
