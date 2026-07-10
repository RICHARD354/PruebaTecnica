import sqlite3

def obtener_conexion():
    """
    Devuelve una conexión a la base de datos.
    """
    return sqlite3.connect("hospital.db")