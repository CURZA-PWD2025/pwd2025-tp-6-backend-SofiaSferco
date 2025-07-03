from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tienda.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .marcas.routes import marca_bp
    from .articulos.routes import articulo_bp
    from .categorias.routes import categoria_bp
    from .proveedores.routes import proveedor_bp

    app.register_blueprint(marca_bp, url_prefix='/marcas')
    app.register_blueprint(articulo_bp, url_prefix='/articulos')
    app.register_blueprint(categoria_bp, url_prefix='/categorias')
    app.register_blueprint(proveedor_bp, url_prefix='/proveedores')

    return app
