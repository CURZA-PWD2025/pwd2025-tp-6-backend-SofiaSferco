from ...database.connect_db import connectDB

class CategoriasModel:
    
    def __init__(self, id:int=0, nombre:str=""):
        self.id=id
        self.nombre=nombre
        

    def serializar(self) -> dict:
        return {
        "id":self.id,
        "nombre":self.nombre
    }
        
    @staticmethod
    def deserializar(data:dict):
        return CategoriasModel(
            id=data["id"], nombre=data["nombre"]
        )
        
        
    @staticmethod    
    def getall():
        cnx = connectDB.get_connect()                         #se conecta a la base de datos
        with cnx.cursor(dictionary=True) as cursor:           #con with es una estructura que asegura de cerrar el cursor,crea un cursor (es el objeto que utilizas para # ejecutar la consulta SQL), dict=True hace que cada tupla venga como un diccionario   
            try:                                              #es una estructura del lenguaje (como if o for) que sirve para probar si hay un error, python no se detiene
                cursor.execute("SELECT * FROM CATEGORIAS")    #ejecuta la consulta
                rows = cursor.fetchall()                      #trae todas las filas de las consultas que viene en forma de diccionario y las coloca en una lista
                marcas = []                                   #se crea la lista vacia
                if rows:                                      #chequea que no este vacio
                    for row in rows:                          #recorre cada elemento de la lista
                        marcas.append(row)                    #lo agrega a marcas
                    return marcas                             #devuelve la lista con todos los elementos copiados
                return False                                  #en caso que no se de la primera condicion se retorna falso
            except Exception as exc:                          #es la 2/3 pata del bloque try por si falla
                print(f"error al listar marca {exc}")         #y aqui se declara que quieres que te devuelva en caso de error
            finally:                                          #es una clausula que si o si debe darse independientemente si funciono el try o no
                cnx.close()                                   #cierra la conexion a la base de datos
                
    @staticmethod
    def get_by_id(id):
        cnx = connectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                print(id)
                cursor.execute("SELECT * FROM CATEGORIAS where id = %s", (id,)) #ejecuta la query
                row = cursor.fetchone() #guarda en una  variable en un resultado
                if row:
                    return row
                return False 
            except Exception as exc:
                print(f"error al listar marca {exc}")
                return False
            finally:
                cnx.close()#cierra la conexion
    
    def create(self):
        cnx = connectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                #ejecuta la query
                cursor.execute("INSERT INTO CATEGORIAS (nombre) values (%s)", (self.nombre,))
                #guarda en una  variable en un resultado
                result = cursor.rowcount
                self.id = cursor.lastrowid
                cnx.commit()
                #alternativa 2  self.id = cursor.lastrowid
                #alternativa 2  if cursor.lastrowid:
                #alternativa 2      return self.serializar()
                #alternativa 2  return False
                
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                print(f"error al listar marca {exc}")
            finally:
                cnx.close()
                
    def update(self):
        cnx = connectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                #ejecuta la query
                cursor.execute("UPDATE CATEGORIAS SET nombre = %s where id=%s", (self.nombre, self.id))
                #guarda en una  variable en un resultado
                result = cursor.rowcount
                cnx.commit()

                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                print(f"error al listar marca {exc}")
            finally:
                cnx.close()
    
    
    def delete(id:int):
        cnx = connectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                #ejecuta la query
                cursor.execute("DELETE FROM CATEGORIAS where id=%s", (id,))
                #guarda en una  variable en un resultado
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                print(f"error al listar marca {exc}")
            finally:
                cnx.close()
                

