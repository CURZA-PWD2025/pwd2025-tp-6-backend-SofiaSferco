from app.db_config import get_db_connection

class ArticuloModel:
    def __init__(self, id=None, nombre=None, precio=None, stock=None, categoria_id=None, marca_id=None, proveedor_id=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria_id = categoria_id
        self.marca_id = marca_id
        self.proveedor_id = proveedor_id

    def serializar(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "categoria_id": self.categoria_id,
            "marca_id": self.marca_id,
            "proveedor_id": self.proveedor_id
        }

    @staticmethod
    def deserializar(data):
        return ArticuloModel(
            id=data.get("id"),
            nombre=data.get("nombre"),
            precio=data.get("precio"),
            stock=data.get("stock"),
            categoria_id=data.get("categoria_id"),
            marca_id=data.get("marca_id"),
            proveedor_id=data.get("proveedor_id")
        )

    @staticmethod
    def get_all():
        conexion = get_db_connection()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ARTICULOS")
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado

    @staticmethod
    def get_one(id):
        conexion = get_db_connection()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ARTICULOS WHERE id = %s", (id,))
        articulo = cursor.fetchone()
        cursor.close()
        conexion.close()
        return articulo

    def create(self):
        conexion = get_db_connection()
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "INSERT INTO ARTICULOS (nombre, precio, stock, categoria_id, marca_id, proveedor_id) VALUES (%s, %s, %s, %s, %s, %s)",
                (self.nombre, self.precio, self.stock, self.categoria_id, self.marca_id, self.proveedor_id)
            )
            conexion.commit()
            self.id = cursor.lastrowid
            return True
        except:
            conexion.rollback()
            return False
        finally:
            cursor.close()
            conexion.close()

    def update(self):
        conexion = get_db_connection()
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "UPDATE ARTICULOS SET nombre=%s, precio=%s, stock=%s, categoria_id=%s, marca_id=%s, proveedor_id=%s WHERE id=%s",
                (self.nombre, self.precio, self.stock, self.categoria_id, self.marca_id, self.proveedor_id, self.id)
            )
            conexion.commit()
            return cursor.rowcount > 0
        except:
            conexion.rollback()
            return False
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def delete(id):
        conexion = get_db_connection()
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM ARTICULOS WHERE id = %s", (id,))
            conexion.commit()
            return cursor.rowcount > 0
        except:
            conexion.rollback()
            return False
        finally:
            cursor.close()
            conexion.close()


