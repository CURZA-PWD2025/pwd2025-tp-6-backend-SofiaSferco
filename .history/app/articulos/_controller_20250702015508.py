from app.articulos._model import ArticuloModel

class ArticuloController:
    @staticmethod
    def get_all():
        # Devuelve lista de objetos ArticuloModel
        return [articulo.serializar() for articulo in ArticuloModel.get_all()]

    @staticmethod
    def get_one(id):
        articulo = ArticuloModel.get_one(id)
        if articulo:
            return articulo.serializar()
        return None

    @staticmethod
    def create(data):
        try:
            articulo = ArticuloModel.deserializar(data)
            articulo.create()
            return articulo.serializar()
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update(id, data):
        articulo = ArticuloModel.query.get(id)
        if articulo:
            articulo.update(data)
            return articulo.serializar()
        return {"error": "Artículo no encontrado"}

    @staticmethod
    def delete(id):
        articulo = ArticuloModel.query.get(id)
        if articulo:
            articulo.delete()
            return {"message": "Artículo eliminado"}
        return {"error": "Artículo no encontrado"}



