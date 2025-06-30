from .articulo_model import ArticuloModel
from ..marca.marca_model import MarcaModel as Marca
from ..proveedores.proveedores_model import ProveedoresModel as Proveedor
from ..categorias.categoria_model import CategoriasModel as Categoria


class ArticulosController:

    @staticmethod
    def get_all():  # define el nombre del controlador 
        articulos = ArticuloModel.get_all()# coloca en una variable el resultado de la funcion getall en categoriasmodel
        return articulos  # devuelve la variable

    @staticmethod
    def get_one(id):
        articulo = ArticuloModel.get_by_id(id=id)
        return articulo


    @staticmethod
    def create(data: dict):
        print("Data recibida en create:", data)
        
        
        categorias_ids = data['categorias']  
        marca = Marca(id=data['marca_id'])
        proveedor = Proveedor(id=data['proveedor_id'])
    
        categorias = []
        for cat_id in categorias_ids:
            cat = Categoria(id=cat_id)
            categorias.append(cat)
    
        data['categorias'] = categorias
        data['marca'] = marca
        data['proveedor'] = proveedor
    
        articulo = ArticuloModel(
            descripcion=data['descripcion'],             
            precio=data['precio'],
            stock=data['stock'],                                
            marca=data['marca'],
            proveedor=data['proveedor'],
            categorias=data['categorias']
            ).create()
    
        return articulo
    

            
    @staticmethod
    def update(data: dict):
        categorias_ids = data['categorias']
        marca_id = data['marca_id']
        proveedor_id = data['proveedor_id']

        marca = Marca(id=marca_id)
        proveedor = Proveedor(id=proveedor_id)
        categorias = [Categoria(id=c) for c in categorias_ids]

        nuevo_data = {
            'id': data['id'],
            'descripcion': data['descripcion'],
            'precio': data['precio'],
            'stock': data['stock'],
            'marca': marca,
            'proveedor': proveedor,
            'categorias': categorias
        }

        articulo = ArticuloModel.deserializar(nuevo_data).update()
        return articulo

    @staticmethod
    def delete(id):
        articulo = ArticuloModel(id=id).delete()
        return articulo
