from .marca_model import MarcaModel

class MarcaController:
    
    @staticmethod
    def get_all():
        marcas = MarcaModel.getall()
        return marcas
    @staticmethod
    def get_one(id):
        marca = MarcaModel.get_by_id(id=id)
        return marca
    @staticmethod
    def create(data:dict):
        marca =MarcaModel(nombre=data['nombre'])
        return marca.create()
    @staticmethod
    def update(data:dict):
        marca =MarcaModel(id=data['id'], nombre=data['nombre'])
        return marca.update()
    @staticmethod
    def delete(id):
        resultado = MarcaModel.delete(id)
        return resultado
        