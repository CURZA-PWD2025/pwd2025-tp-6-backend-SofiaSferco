from app.articulo_model import ArticuloModel

class ArticuloController:
    @staticmethod
    def get_all():
        return ArticuloModel.get_all()

    @staticmethod
    def get_one(id):
        return ArticuloModel.get_one(id)

    @staticmethod
    def create(data):
        articulo = ArticuloModel.deserializar(data)
        articulo.create()
        return articulo.serializar()

    @staticmethod
    def update(id, data):
        articulo = ArticuloModel.query.get(id)
        if articulo:
            articulo.update(data)
            return articulo.serializar()
        return None

    @staticmethod
    def delete(id):
        articulo = ArticuloModel.query.get(id)
        if articulo:
            articulo.delete()
            return {"message": "Artículo eliminado"}
        return {"error": "Artículo no encontrado"}



