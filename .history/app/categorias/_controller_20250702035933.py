from ._model import CategoriaModel

class CategoriaController:
    @staticmethod
    def get_all():
        datos = CategoriaModel.get_all()
        return datos, 200

    @staticmethod
    def get_one(id):
        categoria = CategoriaModel.get_one(id)
        if categoria:
            return categoria, 200
        return {"error": "No se encontró la categoría"}, 404

    @staticmethod
    def create(data):
        if "nombre" not in data:
            return {"error": "Falta campo nombre"}, 400
        nueva = CategoriaModel.deserializar(data)
        if nueva.create():
            return nueva.serializar(), 201
        return {"error": "No se creó la categoría"}, 500

    @staticmethod
    def update(id, data):
        if not CategoriaModel.get_one(id):
            return {"error": "No se encontró la categoría"}, 404
        data["id"] = id
        categoria = CategoriaModel.deserializar(data)
        if categoria.update():
            return categoria.serializar(), 200
        return {"error": "No se actualizó la categoría"}, 500

    @staticmethod
    def delete(id):
        if not CategoriaModel.get_one(id):
            return {"error": "No se encontró la categoría"}, 404
        if CategoriaModel.delete(id):
            return {"message": "Se eliminó la categoría"}, 200
        return {"error": "No se eliminó la categoría"}, 500


