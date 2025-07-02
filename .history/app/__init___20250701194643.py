import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Cargar variables del entorno
load_dotenv(".env-dev") 

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.marcas._routes import marca_bp
    from app.articulos._routes import articulo_bp
    from app.categorias._routes import categoria_bp
    from app.proveedores._routes import proveedor_bp

    app.register_blueprint(marca_bp, url_prefix='/marcas')
    app.register_blueprint(articulo_bp, url_prefix='/articulos')
    app.register_blueprint(categoria_bp, url_prefix='/categorias')
    app.register_blueprint(proveedor_bp, url_prefix='/proveedores')

    return app
