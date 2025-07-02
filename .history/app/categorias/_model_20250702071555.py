from app.config import get_db_connection

class CategoriaModel:
    def __init__(self, id=None, nombre=None):
        self.id = id
        self.nombre = nombre

    def serializar(self):
        return {"id": self.id, "nombre": self.nombre}

    @staticmethod
    def deserializar(data):
        return CategoriaModel(id=data.get("id"), nombre=data.get("nombre"))

    @staticmethod
    def get_all():
        conn = get_db_connection()
        if not conn: return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM CATEGORIAS")
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return datos

    @staticmethod
    def get_one(id):
        conn = get_db_connection()
        if not conn: return None
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM CATEGORIAS WHERE id = %s", (id,))
        categoria = cursor.fetchone()
        cursor.close()
        conn.close()
        return categoria

    def create(self):
        conn = get_db_connection()
        if not conn: return False
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO CATEGORIAS (nombre) VALUES (%s)", (self.nombre,))
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
            cursor.execute("UPDATE CATEGORIAS SET nombre = %s WHERE id = %s", (self.nombre, self.id))
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
            cursor.execute("DELETE FROM CATEGORIAS WHERE id = %s", (id,))
            conn.commit()
            return cursor.rowcount > 0
        except:
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
