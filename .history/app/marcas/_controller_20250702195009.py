from ._model import MarcaModel

class MarcaController:
    @staticmethod
    def get_all():
        return MarcaModel.get_all(), 200

    @staticmethod
    def get_one(id):
        marca = MarcaModel.get_one(id)
        if marca:
            return marca, 200
        return {"error": "Marca no encontrada"}, 404

    @staticmethod
    def create(data):
        if "nombre" not in data:
            return {"error": "Campo 'nombre' requerido"}, 400
        marca = MarcaModel.deserializar(data)
        if marca.create():
            return marca.serializar(), 201
        return {"error": "Error al crear"}, 500

    @staticmethod
    def update(id, data):
        if not MarcaModel.get_one(id):
            return {"error": "Marca no encontrada"}, 404
        data["id"] = id
        marca = MarcaModel.deserializar(data)
        if marca.update():
            return marca.serializar(), 200
        return {"error": "Error al actualizar"}, 500

    @staticmethod
    def delete(id):
        if not MarcaModel.get_one(id):
            return {"error": "Marca no encontrada"}, 404
        if MarcaModel.delete(id):
            return {"mensaje": "Eliminado"}, 200
        return {"error": "Error al eliminar"}, 500