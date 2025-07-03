from flask import Blueprint, request, jsonify
from ._controller import CategoriaController

categorias_bp = Blueprint("categorias", __name__)

@categorias_bp.route("/", methods=["GET"])
def get_all():
    r, s = CategoriaController.get_all()
    return jsonify(r), s

@categorias_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    r, s = CategoriaController.get_one(id)
    return jsonify(r), s

@categorias_bp.route("/", methods=["POST"])
def create():
    r, s = CategoriaController.create(request.get_json())
    return jsonify(r), s

@categorias_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    r, s = CategoriaController.update(id, request.get_json())
    return jsonify(r), s

@categorias_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    r, s = CategoriaController.delete(id)
    return jsonify(r), s
