from app import db

class ArticuloModel(db.Model):
    __tablename__ = 'articulos'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    marca_id = db.Column(db.Integer, db.ForeignKey('marcas.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedores.id'), nullable=False)

    marca = db.relationship('MarcaModel', backref='articulos')
    proveedor = db.relationship('ProveedorModel', backref='articulos')

    def serializar(self):
        return {
            'id': self.id,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'stock': self.stock,
            'marca_id': self.marca_id,
            'proveedor_id': self.proveedor_id
        }

    @staticmethod
    def deserializar(data):
        return ArticuloModel(
            descripcion=data.get('descripcion'),
            precio=data.get('precio'),
            stock=data.get('stock'),
            marca_id=data.get('marca_id'),
            proveedor_id=data.get('proveedor_id')
        )


