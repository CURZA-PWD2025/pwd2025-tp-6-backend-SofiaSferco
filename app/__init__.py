from flask import Flask
from app.modules.marca.marca_routes import marca_bp
from app.modules.categorias.categoria_routes import categoria_bp
from app.modules.proveedores.proveedores_routes import proveedores_bp
from app.modules.articulos.articulo_routes import articulos_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(marca_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(proveedores_bp)
    app.register_blueprint(articulos_bp)
    @app.route("/")
    def home():
        return "<h1>Hola Mundo!</h1>"
    return app