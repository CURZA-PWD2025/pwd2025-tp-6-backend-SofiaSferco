from app.app import db
from app.proveedores._model import ProveedorModel

class ProveedorController:

    @staticmethod
    def get_all():
        return [p.serializar() for p in ProveedorModel.query.all()]

    @staticmethod
    def get_one(id):
        proveedor = ProveedorModel.query.get(id)
        return proveedor.serializar() if proveedor else None

    @staticmethod
    def create(data):
        proveedor = ProveedorModel.deserializar(data)
        db.session.add(proveedor)
        db.session.commit()
        return proveedor.serializar()

    @staticmethod
    def update(id, data):
        proveedor = ProveedorModel.query.get(id)
        if not proveedor:
            return None

        proveedor.nombre = data.get('nombre', proveedor.nombre)
        proveedor.telefono = data.get('telefono', proveedor.telefono)
        proveedor.direccion = data.get('direccion', proveedor.direccion)
        proveedor.email = data.get('email', proveedor.email)

        db.session.commit()
        return proveedor.serializar()

    @staticmethod
    def delete(id):
        proveedor = ProveedorModel.query.get(id)
        if not proveedor:
            return False
        db.session.delete(proveedor)
        db.session.commit()
        return True

