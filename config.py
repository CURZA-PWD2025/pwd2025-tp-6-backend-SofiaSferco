import os
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///tienda.db"      
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
