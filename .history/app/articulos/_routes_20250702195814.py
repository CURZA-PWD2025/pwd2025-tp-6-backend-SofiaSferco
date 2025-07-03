from flask import Blueprint, request, jsonify
from ._controller import ArticuloController

articulos_bp = Blueprint("articulos", __name__)

@articulos_bp.route("/", methods=["GET"])
def get_all():
    r, s = ArticuloController.get_all()
    return jsonify(r), s

@articulos_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    r, s = ArticuloController.get_one(id)
    return jsonify(r), s

@articulos_bp.route("/", methods=["POST"])
def create():
    r, s = ArticuloController.create(request.get_json())
    return jsonify(r), s

@articulos_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    r, s = ArticuloController.update(id, request.get_json())
    return jsonify(r), s

@articulos_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    r, s = ArticuloController.delete(id)
    return jsonify(r), s
