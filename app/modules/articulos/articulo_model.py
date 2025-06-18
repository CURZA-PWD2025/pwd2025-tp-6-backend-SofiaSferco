from app.database.connect_db import connectDB
from ..marca.marca_model import MarcaModel as Marca
from ..proveedores.proveedores_model import ProveedoresModel as Proveedor
from .. categorias.categoria_model import CategoriasModel as Categoria


class ArticuloModel:

    def __init__(self, id: int = 0, descripcion: str = "", precio: float = "", stock: int = "", marca: Marca = None, proveedor: Proveedor = None, categorias: list[Categoria] = None):
        self.id = id
        self.descripcion = descripcion
        self.precio = float(precio) if precio not in (None, "") else 0.0
        self.stock = int(stock) if stock not in (None, "") else 0
        self.marca = marca
        self.proveedor = proveedor
        self.categorias = categorias

    def serializar(self) -> dict:
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "marca": self.marca.serializar(),
            "proveedor": self.proveedor.serializar(),
            "categorias": [categoria.serializar() for categoria in self.categorias]


        }

    @staticmethod
    def deserializar(data: dict) -> 'ArticuloModel':
        return ArticuloModel(
            **data
        )




    @staticmethod
    def get_all():
        cnx = connectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM ARTICULOS"
            cursor.execute(sql)
            resultado =cursor.fetchall()
            if resultado:
                articulos: list=[]
                for row in resultado:
                    marca = Marca.get_by_id(row['marca_id'])
                    proveedor = Proveedor.get_by_id(row['proveedor_id'])
                    categorias = ArticuloModel.get_categorias(row['id'])
                    row['marca'] = marca
                    row['proveedor'] = proveedor
                    row['categoria'] = categorias    
                    del row['marca_id']
                    del row['proveedor_id']
                    articulos.append(row)
            cnx.close()
            return articulos
        
        
    def get_categorias(id) -> list[dict]:
        cnx = connectDB.get_connect()
        categorias = []

        try:
            with cnx.cursor(dictionary=True) as cursor:
            # Paso 1: traer los IDs de categoría desde la tabla intermedia
                sql = "SELECT categoria_id FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s"
                cursor.execute(sql, (id,))
                result = cursor.fetchall()
            
                if result:
                    categoria_ids = [row['categoria_id'] for row in result]

                # Paso 2: si hay IDs, consultamos la tabla CATEGORIAS
                    if categoria_ids:
                        formato = ','.join(['%s'] * len(categoria_ids))
                        sql_categorias = f"SELECT id, nombre FROM CATEGORIAS WHERE id IN ({formato})"
                        cursor.execute(sql_categorias, categoria_ids)
                        categorias = cursor.fetchall()
        finally:
            cnx.close()

        return categorias
        
    @staticmethod
    def get_by_id(id):
        cnx = connectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            print(id)
            try:
                cursor.execute("SELECT * FROM ARTICULOS where id = %s", (id,)) #ejecuta la query
                row = cursor.fetchone() #guarda en una  variable en un resultado
                
                if row:
                    marca = Marca.get_by_id(row['marca_id'])
                    proveedor = Proveedor.get_by_id(row['proveedor_id'])
                    categorias = ArticuloModel.get_categorias(row['id'])
                    row['marca'] = marca
                    row['proveedor'] = proveedor
                    row['categoria'] = categorias    
                    del row['marca_id']
                    del row['proveedor_id']
                    return row
                return False 
            except Exception as exc:
                print(f"error al listar marca {exc}")
                return False
            finally:
                cnx.close()#cierra la conexion



    #CREATE----------------------------------------------------------------------
    def create(self):
        try:
            sql = "INSERT INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id) VALUES (%s, %s, %s, %s, %s)"
            params = (self.descripcion, self.precio, self.stock, self.marca.id, self.proveedor.id)
            print("SQL a ejecutar:", sql)
            print("Parametros:", params)
            
            self.id = connectDB.write(sql, params)
            self.add_categorias()
            return True
        except Exception as e:
            print(f"Error al crear artículo: {e}")
        return False

    def add_categorias(self):
        #self.del_categorias()
        try:
            print("Categorías a agregar:", self.categorias)
            sql = "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (%s, %s)"
            for categoria in self.categorias:
                params = (self.id, categoria.id) 
                result = connectDB.write(sql, params)
                if result:
                    print(f"Categoría {categoria.id} agregada correctamente")
        except Exception as e:
            print("Error al agregar categorías:", e)

    def del_categorias(self):
        try:
            sql = "DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s"
            params = (self.id,)
            result = connectDB.write(sql, params)
            if result:
                print("Categorías eliminadas correctamente")
        except:
            print("Error al eliminar categorías")


    #UPDATE---------------------------------------------------------------------

    def update(self):
        cnx = connectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                sql="UPDATE ARTICULOS SET descripcion = %s, precio =%s, stock =%s, marca_id=%s, proveedor_id=%s WHERE id=%s"
                parametros=(self.descripcion, self.precio, self.stock,self.marca.id, self.proveedor.id, self.id)
                cursor.execute(sql, parametros)
                cnx.commit()
                self.del_categorias()
                self.add_categorias()
                return True
                
            except Exception as exc:
                cnx.rollback()
                print(f"error al actualizar el articulo {exc}")
            finally:
                cnx.close()
                
    def delete(self):
        self.del_categorias()
        sql="DELETE FROM ARTICULOS WHERE id=%s"
        params=(self.id,)
        result=connectDB.write(sql, params)
        if result:
            return True
        else:
            return False
















