from app.db_config import get_db_connection
import mysql.connector

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
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM CATEGORIAS")
        resultado = cursor.fetchall()
        cursor.close()
        db.close()
        return resultado

    @staticmethod
    def get_one(id):
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM CATEGORIAS WHERE id = %s", (id,))
        resultado = cursor.fetchone()
        cursor.close()
        db.close()
        return resultado

    def create(self):
        db = get_db_connection()
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO CATEGORIAS (nombre) VALUES (%s)", (self.nombre,))
            db.commit()
            self.id = cursor.lastrowid
            return True
        except:
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()

    def update(self):
        db = get_db_connection()
        cursor = db.cursor()
        try:
            cursor.execute("UPDATE CATEGORIAS SET nombre=%s WHERE id=%s", (self.nombre, self.id))
            db.commit()
            return cursor.rowcount > 0
        except:
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def delete(id):
        db = get_db_connection()
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM CATEGORIAS WHERE id=%s", (id,))
            db.commit()
            return cursor.rowcount > 0
        except:
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()
