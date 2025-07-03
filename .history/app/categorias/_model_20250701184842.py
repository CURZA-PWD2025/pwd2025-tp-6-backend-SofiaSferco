from app import db

class CategoriaModel(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100), nullable=False)

    def serializar(self):
        return {
            'id': self.id,
            'descripcion': self.descripcion
        }

    @staticmethod
    def deserializar(data):
        return CategoriaModel(
            descripcion=data.get('descripcion')
        )

