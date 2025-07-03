from app.db_config import get_db_connection

class ArticuloModel:
    def __init__(self, id=None, nombre=None, descripcion=None, precio=None, stock=None, categoria_id=None, proveedor_id=None, marca_id=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria_id = categoria_id
        self.proveedor_id = proveedor_id
        self.marca_id = marca_id

    def serializar(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "categoria_id": self.categoria_id,
            "proveedor_id": self.proveedor_id,
            "marca_id": self.marca_id
        }

    @staticmethod
    def deserializar(data):
        return ArticuloModel(
            id=data.get("id"),
            nombre=data.get("nombre"),
            descripcion=data.get("descripcion"),
            precio=data.get("precio"),
            stock=data.get("stock"),
            categoria_id=data.get("categoria_id"),
            proveedor_id=data.get("proveedor_id"),
            marca_id=data.get("marca_id")
        )

    @staticmethod
    def get_all():
        conn = get_db_connection()
        if not conn: return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ARTICULOS")
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultado

    @staticmethod
    def get_one(id):
        conn = get_db_connection()
        if not conn: return None
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ARTICULOS WHERE id = %s", (id,))
        articulo = cursor.fetchone()
        cursor.close()
        conn.close()
        return articulo

    def create(self):
        conn = get_db_connection()
        if not conn: return False
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO ARTICULOS (nombre, descripcion, precio, stock, categoria_id, proveedor_id, marca_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                self.nombre, self.descripcion, self.precio, self.stock,
                self.categoria_id, self.proveedor_id, self.marca_id
            ))
            conn.commit()
            self.id = cursor.lastrowid
            return True
        except:
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    def update(self):
        conn = get_db_connection()
        if not conn: return False
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE ARTICULOS
                SET nombre = %s, descripcion = %s, precio = %s, stock = %s,
                    categoria_id = %s, proveedor_id = %s, marca_id = %s
                WHERE id = %s
            """, (
                self.nombre, self.descripcion, self.precio, self.stock,
                self.categoria_id, self.proveedor_id, self.marca_id, self.id
            ))
            conn.commit()
            return cursor.rowcount > 0
        except:
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete(id):
        conn = get_db_connection()
        if not conn: return False
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM ARTICULOS WHERE id = %s", (id,))
            conn.commit()
            return cursor.rowcount > 0
        except:
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
