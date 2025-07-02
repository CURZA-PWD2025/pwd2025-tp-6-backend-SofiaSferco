from ._model import ArticuloModel

class ArticuloController:
    @staticmethod
    def get_all():
        datos = ArticuloModel.get_all()
        return datos, 200

    @staticmethod
    def get_one(id):
        articulo = ArticuloModel.get_one(id)
        if articulo:
            return articulo, 200
        return {"error": "Artículo no encontrado"}, 404

    @staticmethod
    def create(data):
        campos = ["nombre", "precio", "stock", "categoria_id", "marca_id", "proveedor_id"]
        if not all(c in data for c in campos):
            return {"error": "Faltan campos obligatorios"}, 400
        nuevo = ArticuloModel.deserializar(data)
        if nuevo.create():
            return nuevo.serializar(), 201
        return {"error": "No se pudo crear el artículo"}, 500

    @staticmethod
    def update(id, data):
        if not ArticuloModel.get_one(id):
            return {"error": "Artículo no encontrado"}, 404
        data["id"] = id
        articulo = ArticuloModel.deserializar(data)
        if articulo.update():
            return articulo.serializar(), 200
        return {"error": "No se pudo actualizar el artículo"}, 500

    @staticmethod
    def delete(id):
        if not ArticuloModel.get_one(id):
            return {"error": "Artículo no encontrado"}, 404
        if ArticuloModel.delete(id):
            return {"message": "Artículo eliminado con éxito"}, 200
        return {"error": "No se pudo eliminar el artículo"}, 500



