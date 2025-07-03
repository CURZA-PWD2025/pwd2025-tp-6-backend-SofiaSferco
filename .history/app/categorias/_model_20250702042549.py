from app.db_config import get_db_connection

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
        conn = get_db_connection()
        if not conn: return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM PROVEEDORES")
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultado

    @staticmethod
    def get_one(id):
        conn = get_db_connection()
        if not conn: return None
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM PROVEEDORES WHERE id = %s", (id,))
        proveedor = cursor.fetchone()
        cursor.close()
        conn.close()
        return proveedor

    def create(self):
        conn = get_db_connection()
        if not conn: return False
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO PROVEEDORES (nombre, telefono, direccion, email) VALUES (%s, %s, %s, %s)",
                (self.nombre, self.telefono, self.direccion, self.email)
            )
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
            cursor.execute(
                "UPDATE PROVEEDORES SET nombre=%s, telefono=%s, direccion=%s, email=%s WHERE id=%s",
                (self.nombre, self.telefono, self.direccion, self.email, self.id)
            )
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
            cursor.execute("DELETE FROM PROVEEDORES WHERE id = %s", (id,))
            conn.commit()
            return cursor.rowcount > 0
        except:
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

