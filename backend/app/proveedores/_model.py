from app.db_config import get_db_connection
import mysql.connector

class ProveedorModel:
    def __init__(self, id=None, nombre=None, telefono=None, direccion=None, email=None):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

    def serializar(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "email": self.email
        }

    @staticmethod
    def deserializar(data):
        return ProveedorModel(
            id=data.get("id"),
            nombre=data.get("nombre"),
            telefono=data.get("telefono"),
            direccion=data.get("direccion"),
            email=data.get("email")
        )

    @staticmethod
    def get_all():
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM PROVEEDORES")
        resultado = cursor.fetchall()
        cursor.close()
        db.close()
        return resultado

    @staticmethod
    def get_one(id):
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM PROVEEDORES WHERE id = %s", (id,))
        resultado = cursor.fetchone()
        cursor.close()
        db.close()
        return resultado

    def create(self):
        db = get_db_connection()
        cursor = db.cursor()
        try:
            cursor.execute("""
                INSERT INTO PROVEEDORES (nombre, telefono, direccion, email)
                VALUES (%s, %s, %s, %s)
            """, (self.nombre, self.telefono, self.direccion, self.email))
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
            cursor.execute("""
                UPDATE PROVEEDORES
                SET nombre=%s, telefono=%s, direccion=%s, email=%s
                WHERE id=%s
            """, (self.nombre, self.telefono, self.direccion, self.email, self.id))
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
            cursor.execute("DELETE FROM PROVEEDORES WHERE id = %s", (id,))
            db.commit()
            return cursor.rowcount > 0
        except:
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()
