import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector.pooling import MySQLConnectionPool

load_dotenv()
class ConexionDB:
    pool = None

    @classmethod
    def inicializar_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = MySQLConnectionPool(
                    pool_name="pool_tienda",
                    pool_size=4,
                    host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD"),
                    database=os.getenv("DB_NAME"),
                    port=int(os.getenv("DB_PORT") or 3306)
                )
                print("Pool de conexiones iniciado")
            except mysql.connector.Error as err:
                print(f"Error al crear el pool: {err}")
                cls.pool = None

    @classmethod
    def obtener_conexion(cls):
        if cls.pool is None:
            cls.inicializar_pool()
        if cls.pool:
            try:
                return cls.pool.get_connection()
            except mysql.connector.Error as err:
                print(f"Error al obtener conexión: {err}")
                return None
        else:
            return None

# Función externa para importar desde los modelos
def get_db_connection():
    return ConexionDB.obtener_conexion()

