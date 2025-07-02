from app.db_config import get_db_connection
import mysql.connector

class MarcaModel:
    def __init__(self, id=None, nombre=None):
        self.id = id
        self.nombre = nombre

    def serializar(self):
        return {"id": self.id, "nombre": self.nombre}

    @staticmethod
    def deserializar(data):
        return MarcaModel(
            id=data.get("id"),
            nombre=data.get("nombre")
        )

    @staticmethod
    def get_all():
        conexion = get_db_connection()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM MARCAS")
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado

    @staticmethod
    def get_one(id):
        conexion = get_db_connection()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM MARCAS WHERE id = %s", (id,))
        marca = cursor.fetchone()
        cursor.close()
        conexion.close()
        return marca

    def create(self):
        conexion = get_db_connection()
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO MARCAS (nombre) VALUES (%s)", (self.nombre,))
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
            cursor.execute("UPDATE MARCAS SET nombre = %s WHERE id = %s", (self.nombre, self.id))
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
            cursor.execute("DELETE FROM MARCAS WHERE id = %s", (id,))
            conexion.commit()
            return cursor.rowcount > 0
        except:
            conexion.rollback()
            return False
        finally:
            cursor.close()
            conexion.close()


