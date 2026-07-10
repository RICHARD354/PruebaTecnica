from database.conexion import obtener_conexion

def crear_base_datos():
    """
    Crea las tablas de la base de datos si no existen.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS doctores(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        nombre TEXT NOT NULL,

        especialidad TEXT NOT NULL

    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        nombre TEXT NOT NULL,

        sintomas TEXT NOT NULL

    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS citas(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        paciente TEXT NOT NULL,

        doctor TEXT NOT NULL,

        especialidad TEXT NOT NULL,

        fecha TEXT NOT NULL,

        hora TEXT NOT NULL

    )
    """)

    conexion.commit()
    conexion.close()