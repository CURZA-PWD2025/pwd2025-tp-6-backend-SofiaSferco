from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from config import Config

db = SQLAlchemy()  # instancia global

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    # Importar blueprints dentro de la función para evitar import circular
    from app.marcas._routes import marca_bp
    from app.categorias._routes import categoria_bp
    from app.proveedores._routes import proveedor_bp
    from app.articulos._routes import articulo_bp

    # Registrar blueprints con prefijos de URL
    app.register_blueprint(marca_bp, url_prefix="/marcas")
    app.register_blueprint(categoria_bp, url_prefix="/categorias")
    app.register_blueprint(proveedor_bp, url_prefix="/proveedores")
    app.register_blueprint(articulo_bp, url_prefix="/articulos")

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        response = jsonify({
            "error": error.description,
            "code": error.code
        })
        response.status_code = error.code
        return response

    return app

