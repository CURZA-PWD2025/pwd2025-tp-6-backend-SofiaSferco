from app import db

class MarcaModel(db.Model):
    __tablename__ = 'marcas'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100), nullable=False)

    def serializar(self):
        return {
            'id': self.id,
            'descripcion': self.descripcion
        }

    @staticmethod
    def deserializar(data):
        return MarcaModel(descripcion=data.get('descripcion'))
