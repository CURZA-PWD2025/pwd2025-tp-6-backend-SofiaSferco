from app import db
from app.articulos._model import ArticuloModel

class ArticuloController:

    @staticmethod
    def get_all():
        articulos = ArticuloModel.query.all()
        return [a.serializar() for a in articulos]

    @staticmethod
    def get_one(id):
        articulo = ArticuloModel.query.get(id)
        return articulo.serializar() if articulo else None

    @staticmethod
    def create(data):
        articulo = ArticuloModel.deserializar(data)
        db.session.add(articulo)
        try:
            db.session.commit()
            return articulo.serializar()
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}

    @staticmethod
    def update(id, data):
        articulo = ArticuloModel.query.get(id)
        if not articulo:
            return None
        for key, value in data.items():
            setattr(articulo, key, value)
        try:
            db.session.commit()
            return articulo.serializar()
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}

    @staticmethod
    def delete(id):
        articulo = ArticuloModel.query.get(id)
        if not articulo:
            return None
        try:
            db.session.delete(articulo)
            db.session.commit()
            return {'message': 'Artículo eliminado'}
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}


