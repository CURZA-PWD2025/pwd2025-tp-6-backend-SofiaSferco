from ._model import CategoriaModel

class CategoriaController:
    @staticmethod
    def get_all():
        return CategoriaModel.get_all(), 200

    @staticmethod
    def get_one(id):
        categoria = CategoriaModel.get_one(id)
        if categoria:
            return categoria, 200
        return {"error": "Categoría no encontrada"}, 404

    @staticmethod
    def create(data):
        if "nombre" not in data:
            return {"error": "Campo 'nombre' requerido"}, 400
        categoria = CategoriaModel.deserializar(data)
        if categoria.create():
            return categoria.serializar(), 201
        return {"error": "Error al crear"}, 500

    @staticmethod
    def update(id, data):
        if not CategoriaModel.get_one(id):
            return {"error": "Categoría no encontrada"}, 404
        data["id"] = id
        categoria = CategoriaModel.deserializar(data)
        if categoria.update():
            return categoria.serializar(), 200
        return {"error": "Error al actualizar"}, 500

    @staticmethod
    def delete(id):
        if not CategoriaModel.get_one(id):
            return {"error": "Categoría no encontrada"}, 404
        if CategoriaModel.delete(id):
            return {"mensaje": "Eliminado"}, 200
        return {"error": "Error al eliminar"}, 500
