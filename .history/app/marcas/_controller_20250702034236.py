from ._model import MarcaModel

class MarcaController:
    @staticmethod
    def get_all():
        datos = MarcaModel.get_all()
        return datos, 200

    @staticmethod
    def get_one(id):
        marca = MarcaModel.get_one(id)
        if marca:
            return marca, 200
        return {"error": "No se encontró la marca"}, 404

    @staticmethod
    def create(data):
        if "nombre" not in data:
            return {"error": "Falta campo nombre"}, 400
        nueva = MarcaModel.deserializar(data)
        if nueva.create():
            return nueva.serializar(), 201
        return {"error": "No se pudo crear"}, 500

    @staticmethod
    def update(id, data):
        existente = MarcaModel.get_one(id)
        if not existente:
            return {"error": "No se encontró la marca"}, 404
        data["id"] = id
        marca = MarcaModel.deserializar(data)
        if marca.update():
            return marca.serializar(), 200
        return {"error": "No se encontró la marca"}, 500

    @staticmethod
    def delete(id):
        if not MarcaModel.get_one(id):
            return {"error": "Marca no encontrada"}, 404
        if MarcaModel.delete(id):
            return {"message": "Eliminado con éxito"}, 200
        return {"error": "No se pudo eliminar"}, 500
