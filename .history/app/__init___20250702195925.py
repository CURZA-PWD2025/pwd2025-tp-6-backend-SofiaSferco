from flask import Flask
from app.articulos._routes import articulos_bp
from app.marcas._routes import marcas_bp
from app.categorias._routes import categorias_bp
from app.proveedores._routes import proveedores_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(articulos_bp, url_prefix="/api/articulos")
    app.register_blueprint(marcas_bp, url_prefix="/api/marcas")
    app.register_blueprint(categorias_bp, url_prefix="/api/categorias")
    app.register_blueprint(proveedores_bp, url_prefix="/api/proveedores")

    return app





