from app import db
from app.categorias._model import CategoriaModel

class CategoriaController:

    @staticmethod
    def get_all():
        return [c.serializar() for c in CategoriaModel.query.all()]

    @staticmethod
    def get_one(id):
        categoria = CategoriaModel.query.get(id)
        return categoria.serializar() if categoria else None

    @staticmethod
    def create(data):
        categoria = CategoriaModel.deserializar(data)
        db.session.add(categoria)
        db.session.commit()
        return categoria.serializar()

    @staticmethod
    def update(id, data):
        categoria = CategoriaModel.query.get(id)
        if not categoria:
            return None
        categoria.descripcion = data.get('descripcion', categoria.descripcion)
        db.session.commit()
        return categoria.serializar()

    @staticmethod
    def delete(id):
        categoria = CategoriaModel.query.get(id)
        if not categoria:
            return False
        db.session.delete(categoria)
        db.session.commit()
        return True

