from app import db

class ArticuloModel(db.Model):
    __tablename__ = 'articulos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_one(cls, id):
        return cls.query.get(id)

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def deserializar(cls, data):
        # Asumimos que data es un dict con las keys coincidentes con los campos
        return cls(**data)

    def serializar(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'stock': self.stock
        }


