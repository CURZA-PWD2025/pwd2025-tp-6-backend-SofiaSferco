from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from config import Config

db = SQLAlchemy()  # <-- se define global, sin app

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)  # <-- esto es clave

    # importar rutas
    from app.marcas._routes import marca_bp
    app.register_blueprint(marca_bp, url_prefix="/marcas")
    
    from routes.categoria_routes import categoria_bp
    app.register_blueprint(categoria_bp, url_prefix="/categorias")

    from routes.proveedor_routes import proveedor_bp
    app.register_blueprint(proveedor_bp, url_prefix="/proveedores")

    from routes.articulo_routes import articulo_bp
    app.register_blueprint(articulo_bp, url_prefix='/articulos')

    # Manejador global para errores HTTP, incluido el 409
    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        response = jsonify({
            "error": error.description,
            "code": error.code
        })
        response.status_code = error.code
        return response

    return app


