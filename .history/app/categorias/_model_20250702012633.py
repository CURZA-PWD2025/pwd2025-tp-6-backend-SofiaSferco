from app import db

class CategoriaModel(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def serializar(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }

    @staticmethod
    def deserializar(data):
        return CategoriaModel(
            nombre=data.get('nombre')
        )


