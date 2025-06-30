from .categoria_model import CategoriasModel

class CategoriaController:
    
    @staticmethod
    def get_all():                               #define el nombre del controlador
        categorias = CategoriasModel.getall()    #coloca en una variable el resultado de la funcion getall en categoriasmodel
        return categorias                        #devuelve la variable
    @staticmethod
    def get_one(id):
        categorias = CategoriasModel.get_by_id(id=id)
        return categorias
    @staticmethod
    def create(data:dict):
        categorias =CategoriasModel(nombre=data['nombre'])
        return categorias.create()
    @staticmethod
    def update(data:dict):
        categorias =CategoriasModel(id=data['id'], nombre=data['nombre'])
        return categorias.update()
    @staticmethod
    def delete(id):
        categorias = CategoriasModel.delete(id)
        return categorias
        