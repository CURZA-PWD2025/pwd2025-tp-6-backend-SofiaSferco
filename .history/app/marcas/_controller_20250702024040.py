from app.marcas._model import MarcaModel
from app.app import db

class MarcaController:

    @staticmethod
    def get_all():
        return [marca.serializar() for marca in MarcaModel.query.all()]

    @staticmethod
    def get_one(id):
        marca = MarcaModel.query.get(id)
        return marca.serializar() if marca else None

    @staticmethod
    def create(data):
        marca = MarcaModel.deserializar(data)
        db.session.add(marca)
        db.session.commit()
        return marca.serializar()

    @staticmethod
    def update(id, data):
        marca = MarcaModel.query.get(id)
        if not marca:
            return None
        marca.descripcion = data.get('descripcion', marca.descripcion)
        db.session.commit()
        return marca.serializar()

    @staticmethod
    def delete(id):
        marca = MarcaModel.query.get(id)
        if not marca:
            return False
        db.session.delete(marca)
        db.session.commit()
        return True
