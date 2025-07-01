from app import db

class ProveedorModel(db.Model):
    __tablename__ = 'proveedores'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def serializar(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'telefono': self.telefono,
            'direccion': self.direccion,
            'email': self.email
        }

    @staticmethod
    def deserializar(data):
        return ProveedorModel(
            nombre=data.get('nombre'),
            telefono=data.get('telefono'),
            direccion=data.get('direccion'),
            email=data.get('email')
        )

