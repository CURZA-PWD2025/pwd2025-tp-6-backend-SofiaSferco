from ...database.connect_db import connectDB


class MarcaModel:
    
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
        return MarcaModel(
            id=data["id"], nombre=data["nombre"]
        )
        
        
    @staticmethod    
    def getall():
        cnx = connectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                #ejecuta la query
                cursor.execute("SELECT * FROM MARCAS")
                #guarda en una  variable en un resultado
                rows = cursor.fetchall()
                #lisa de diccionario
                marcas = []
                if rows:
                    for row in rows:
                        marcas.append(row)
                    return marcas
                return False
            except Exception as exc:
                print(f"error al listar marca {exc}")
            finally:
                cnx.close()
                
    @staticmethod
    def get_by_id(id:int):
        #print(f'aca esta el id de marca')
        cnx = connectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                #ejecuta la query
                cursor.execute("SELECT * FROM MARCAS where id = %s", (id,))
                #guarda en una  variable en un resultado
                row = cursor.fetchone()
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
                cursor.execute("INSERT INTO MARCAS (nombre) values (%s)", (self.nombre,))
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
                cursor.execute("UPDATE MARCAS SET nombre = %s where id=%s", (self.nombre, self.id))
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
                cursor.execute("DELETE FROM MARCAS where id=%s", (id,))
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
    
    @classmethod
    def get_one(cls,id):
        sql = "SELECT * FROM MARCAS where id= %s"
        params = (id,)
        result = connectDB.read(sql, params)
        return result