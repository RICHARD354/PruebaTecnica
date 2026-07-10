from database.conexion import obtener_conexion

def crear_base_datos():
    """
    Crea las tablas de la base de datos si no existen.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS doctores (

        id_doctor INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        especialidad TEXT NOT NULL

    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes(

        id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        sintomas TEXT NOT NULL

    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS citas(

        id_cita INTEGER PRIMARY KEY AUTOINCREMENT,
        id_doctor INTEGER NOT NULL,
        id_paciente INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        hora TEXT NOT NULL,

        FOREIGN KEY(id_doctor)
        REFERENCES doctores(id_doctor),
        FOREIGN KEY(id_paciente)
            REFERENCES pacientes(id_paciente)

    )
    """)

    conexion.commit()
    conexion.close()