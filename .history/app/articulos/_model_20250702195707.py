from app.db_config import get_db_connection
import mysql.connector

class ArticuloModel:
    def __init__(self, id=None, descripcion=None, precio=None, stock=None, marca_id=None, proveedor_id=None, categorias=None):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca_id = marca_id
        self.proveedor_id = proveedor_id
        self.categorias = categorias or []

    def serializar(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "marca_id": self.marca_id,
            "proveedor_id": self.proveedor_id,
            "categorias": self.categorias
        }

    @staticmethod
    def deserializar(data):
        return ArticuloModel(
            id=data.get("id"),
            descripcion=data.get("descripcion"),
            precio=data.get("precio"),
            stock=data.get("stock"),
            marca_id=data.get("marca_id"),
            proveedor_id=data.get("proveedor_id"),
            categorias=data.get("categorias", [])
        )

    @staticmethod
    def get_all():
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ARTICULOS")
        articulos = cursor.fetchall()

        for articulo in articulos:
            cursor.execute("""
                SELECT categoria_id FROM ARTICULOS_CATEGORIAS
                WHERE articulo_id = %s
            """, (articulo["id"],))
            categorias = cursor.fetchall()
            articulo["categorias"] = [c["categoria_id"] for c in categorias]

        cursor.close()
        db.close()
        return articulos

    @staticmethod
    def get_one(id):
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ARTICULOS WHERE id = %s", (id,))
        articulo = cursor.fetchone()
        if articulo:
            cursor.execute("""
                SELECT categoria_id FROM ARTICULOS_CATEGORIAS
                WHERE articulo_id = %s
            """, (id,))
            categorias = cursor.fetchall()
            articulo["categorias"] = [c["categoria_id"] for c in categorias]
        cursor.close()
        db.close()
        return articulo

    def create(self):
        db = get_db_connection()
        cursor = db.cursor()
        try:
            cursor.execute("""
                INSERT INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id))
            db.commit()
            self.id = cursor.lastrowid

            for categoria_id in self.categorias:
