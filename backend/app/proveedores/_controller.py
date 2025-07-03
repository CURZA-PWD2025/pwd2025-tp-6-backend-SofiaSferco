from ._model import ProveedorModel

class ProveedorController:
    @staticmethod
    def get_all():
        return ProveedorModel.get_all(), 200

    @staticmethod
    def get_one(id):
        proveedor = ProveedorModel.get_one(id)
        if proveedor:
            return proveedor, 200
        return {"error": "Proveedor no encontrado"}, 404

    @staticmethod
    def create(data):
        campos = ["nombre", "telefono", "direccion", "email"]
        if not all(c in data for c in campos):
            return {"error": "Faltan campos obligatorios"}, 400
        proveedor = ProveedorModel.deserializar(data)
        if proveedor.create():
            return proveedor.serializar(), 201
        return {"error": "Error al crear"}, 500

    @staticmethod
    def update(id, data):
        if not ProveedorModel.get_one(id):
            return {"error": "Proveedor no encontrado"}, 404
        data["id"] = id
        proveedor = ProveedorModel.deserializar(data)
        if proveedor.update():
            return proveedor.serializar(), 200
        return {"error": "Error al actualizar"}, 500

    @staticmethod
    def delete(id):
        if not ProveedorModel.get_one(id):
            return {"error": "Proveedor no encontrado"}, 404
        if ProveedorModel.delete(id):
            return {"mensaje": "Eliminado"}, 200
        return {"error": "Error al eliminar"}, 500
