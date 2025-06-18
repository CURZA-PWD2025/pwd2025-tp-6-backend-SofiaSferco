from .proveedores_model import ProveedoresModel

class ProveedoresController:
    
    @staticmethod
    def get_all():                               #define el nombre del controlador
        proveedores =ProveedoresModel.getall()    #coloca en una variable el resultado de la funcion getall en categoriasmodel
        return proveedores                        #devuelve la variable
    @staticmethod
    def get_one(id):
        proveedores =ProveedoresModel.get_by_id(id=id)
        return proveedores
    @staticmethod
    def create(data:dict):
        proveedores=ProveedoresModel(nombre=data['nombre'], telefono=data['telefono'], direccion=data['direccion'], email=data['email'],)
        return proveedores.create()
    @staticmethod
    def update(data:dict):
        proveedores=ProveedoresModel(id=data['id'], nombre=data['nombre'], telefono=data['telefono'], direccion=data['direccion'], email=data['email'], )
        return proveedores.update()
    @staticmethod
    def delete(id):
        proveedores =ProveedoresModel.delete(id)
        return proveedores
        