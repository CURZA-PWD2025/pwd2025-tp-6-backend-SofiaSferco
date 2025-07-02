from app import db

class ArticuloModel(db.Model):
    __tablename__ = 'ARTICULOS'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(150), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('MARCAS.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('PROVEEDORES.id'), nullable=False)

    # Si querés, podés agregar relaciones con las otras tablas (opcional)
    marca = db.relationship('MarcaModel', backref='articulos')
    proveedor = db.relationship('ProveedorModel', backref='articulos')

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
        return cls(**data)

    def serializar(self):
        return {
            'id': self.id,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'stock': self.stock,
            'marca_id': self.marca_id,
            'proveedor_id': self.proveedor_id
        }

