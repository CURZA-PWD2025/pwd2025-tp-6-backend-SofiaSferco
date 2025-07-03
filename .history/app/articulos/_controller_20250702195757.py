from ._model import ArticuloModel

class ArticuloController:
    @staticmethod
    def get_all():
        return ArticuloModel.get_all(), 200

    @staticmethod
    def get_one(id):
        articulo = ArticuloModel.get_one(id)
        if articulo:
            return articulo, 200
        return {"error": "Artículo no encontrado"}, 404

    @staticmethod
    def create(data):
        campos = ["descripcion", "precio", "stock", "marca_id", "proveedor_id"]
        if not all(c in data for c in campos):
            return {"error": "Faltan campos obligatorios"}, 400
        articulo = ArticuloModel.deserializar(data)
        if articulo.create():
            return articulo.serializar(), 201
        return {"error": "Error al crear"}, 500

    @staticmethod
    def update(id, data):
        if not ArticuloModel.get_one(id):
            return {"error": "Artículo no encontrado"}, 404
        data["id"] = id
        articulo = ArticuloModel.deserializar(data)
        if articulo.update():
            return articulo.serializar(), 200
        return {"error": "Error al actualizar"}, 500

    @staticmethod
    def delete(id):
        if not ArticuloModel.get_one(id):
            return {"error": "Artículo no encontrado"}, 404
        if ArticuloModel.delete(id):
            return {"mensaje": "Eliminado"}, 200
        return {"error": "Error al eliminar"}, 500
