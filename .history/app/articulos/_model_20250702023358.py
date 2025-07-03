from app import db

articulos_categorias = db.Table(
    'articulos_categorias',
    db.Column('articulo_id', db.Integer, db.ForeignKey('articulos.id'), primary_key=True),
    db.Column('categoria_id', db.Integer, db.ForeignKey('categorias.id'), primary_key=True)
)

class ArticuloModel(db.Model):
    __tablename__ = 'articulos'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(150), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    marca_id = db.Column(db.Integer, db.ForeignKey('marcas.id'), nullable=False)
    marca = db.relationship('MarcaModel')

    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedores.id'), nullable=False)
    proveedor = db.relationship('ProveedorModel')

    categorias = db.relationship('CategoriaModel', secondary=articulos_categorias, backref='articulos')

    def serializar(self):
        return {
            'id': self.id,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'stock': self.stock,
            'marca': self.marca.serializar() if self.marca else None,
            'proveedor': self.proveedor.serializar() if self.proveedor else None,
            'categorias': [cat.serializar() for cat in self.categorias]
        }

    @staticmethod
    def deserializar(data):
        articulo = ArticuloModel(
            descripcion=data.get('descripcion'),
            precio=data.get('precio'),
            stock=data.get('stock'),
            marca_id=data.get('marca_id'),
            proveedor_id=data.get('proveedor_id')
        )
        if 'categorias_ids' in data:
            from app.categorias._model import CategoriaModel
            categorias = CategoriaModel.query.filter(CategoriaModel.id.in_(data['categorias_ids'])).all()
            articulo.categorias = categorias
        return articulo

    @staticmethod
    def get_all():
        return [a.serializar() for a in ArticuloModel.query.all()]

    @staticmethod
    def get_one(id):
        a = ArticuloModel.query.get(id)
        return a.serializar() if a else None

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, value in data.items():
            if key == 'categorias_ids':
                from models.categoria_model import CategoriaModel
                categorias = CategoriaModel.query.filter(CategoriaModel.id.in_(value)).all()
                self.categorias = categorias
            elif hasattr(self, key):
                setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

