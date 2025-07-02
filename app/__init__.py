from flask import Flask
from app.marcas._routes import marcas_bp
from app.categorias._routes import categorias_bp
from app.proveedores._routes import proveedores_bp
from app.articulos._routes import articulos_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(marcas_bp, url_prefix="/marcas")
    app.register_blueprint(categorias_bp, url_prefix="/categorias")
    app.register_blueprint(proveedores_bp, url_prefix="/proveedores")
    app.register_blueprint(articulos_bp, url_prefix="/articulos")

    return app



