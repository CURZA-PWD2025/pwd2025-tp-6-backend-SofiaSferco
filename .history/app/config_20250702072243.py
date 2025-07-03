import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///tienda.db"  # Archivo SQLite local en la raíz del proyecto
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
