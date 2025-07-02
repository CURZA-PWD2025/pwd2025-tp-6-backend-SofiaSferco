import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()

class connectDB:
    @staticmethod
    def get_connect():
        try:
            conn = mysql.connector.connect(
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
                host=os.getenv("DB_HOST","localhost"),
                port=int(os.getenv("DB_PORT", 3306))
            )
            return conn
        except Exception as ex:
            print (f"an exception ocurred {ex}")
    
#print("Conectado a:", os.getenv("DB_NAME"))

    def read(sql: str, params: tuple = None):
        cxn = connectDB.get_connect()
        with cxn.cursor(dictionary=True) as cursor:
            try:
                cursor.execute(sql, params)
                result = cursor.fetchall()
                return result if result else None
            except Error as e:
                print(f'Error {e}')
            finally:
                cxn.close()


    @staticmethod
    def write(sql: str, params: tuple):
        cxn = connectDB.get_connect()
        try:
            with cxn.cursor() as cursor:
                cursor.execute(sql, params)
                cxn.commit()

                if sql.strip().upper().startswith("INSERT"):
                    return cursor.lastrowid  

                return cursor.rowcount > 0  
        except Exception as e:
            print(f"Error en la consulta: {e}")
            return False
        finally:
            cxn.close()