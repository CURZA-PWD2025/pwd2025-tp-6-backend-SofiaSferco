from flask import Flask
from flask_cors import CORS
from app.articulos._routes import articulos_bp
from app.marcas._routes import marcas_bp
from app.categorias._routes import categorias_bp
from app.proveedores._routes import proveedores_bp

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    app.register_blueprint(articulos_bp, url_prefix="/articulos")
    app.register_blueprint(marcas_bp, url_prefix="/marcas")
    app.register_blueprint(categorias_bp, url_prefix="/categorias")
    app.register_blueprint(proveedores_bp, url_prefix="/proveedores")

    return app





