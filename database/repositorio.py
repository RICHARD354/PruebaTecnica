from database.conexion import obtener_conexion
from usuarios.doctor import Doctor
from usuarios.paciente import Paciente
from servicios.cita import Cita

def guardar_doctor(doctor):
    """
    Guarda un doctor en la base de datos.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            """
            INSERT INTO doctores(nombre, especialidad)
            VALUES(?, ?)
            """,
            (
                doctor.nombre,
                doctor.especialidad
            )
        )
        doctor.id_doctor = cursor.lastrowid

        conexion.commit()
    except Exception as e:
        print(f"Error al guardar el doctor: {e}")

    finally:
        if conexion:
            conexion.close()


def guardar_paciente(paciente):
    """
    Guarda un paciente en la base de datos.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            """
            INSERT INTO pacientes(nombre, sintomas)
            VALUES(?, ?)
            """,
            (
                paciente.nombre,
                paciente.sintomas
            )
        )
        paciente.id_paciente = cursor.lastrowid

        conexion.commit()
    except Exception as e:
        print(f"Error al guardar al paciente: {e}")

    finally:
        if conexion:
            conexion.close()

def guardar_cita(cita):
    """
    Guarda una cita en la base de datos.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            """
            INSERT INTO citas(

                id_doctor,
                id_paciente,
                fecha,
                hora

            )
            VALUES(?, ?, ?, ?)
            """,
            (
                cita.doctor.id_doctor,
                cita.paciente.id_paciente,
                cita.fecha,
                cita.hora
            )
        )

        conexion.commit()
    except Exception as e:
        print(f"Error al guardar la cita: {e}")
    finally:
        if conexion:
            conexion.close()

def obtener_doctores():
    """
    Obtiene todos los doctores registrados.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT
                id_doctor,
                nombre,
                especialidad
            FROM doctores
            ORDER BY nombre
        """)

        registros = cursor.fetchall()
        doctores = []
        for id_doctor, nombre, especialidad in registros:
            doctor = Doctor(
                nombre,
                especialidad,
                id_doctor
            )
            doctores.append(doctor)
        
        return doctores
    except sqlite3.Error as e:
        print(f"Error al obtener a los doctores: {e}")
        return []
    finally:
        if conexion:
            conexion.close()
    

def obtener_pacientes():
    """
    Obtiene todos los pacientes registrados.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                id_paciente,
                nombre,
                sintomas
            FROM pacientes
            ORDER BY nombre
        """)

        registros = cursor.fetchall()
        pacientes = []

        for id_paciente, nombre, sintomas in registros:
            paciente = Paciente(
                nombre,
                sintomas,
                id_paciente
            )
            pacientes.append(paciente)

        return pacientes
    except sqlite3.Error as e:
        print(f"Error al obtener a los pacientes: {e}")
        return []
    finally:
        if conexion:
            conexion.close()

def obtener_citas():
    """
    Obtiene todas las citas registradas.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                c.id_cita,
                c.fecha,
                c.hora,
                d.id_doctor,
                d.nombre,
                d.especialidad,
                p.id_paciente,
                p.nombre,
                p.sintomas

            FROM citas c
            INNER JOIN doctores d
                ON c.id_doctor = d.id_doctor
            INNER JOIN pacientes p
                ON c.id_paciente = p.id_paciente
            ORDER BY c.fecha, c.hora
        """)

        registros = cursor.fetchall()

        citas = []

        for (
            id_cita,
            fecha,
            hora,
            id_doctor,
            nombre_doctor,
            especialidad,
            id_paciente,
            nombre_paciente,
            sintomas
        ) in registros:
            doctor = Doctor(
                nombre_doctor,
                especialidad,
                id_doctor
            )

            paciente = Paciente(
                nombre_paciente,
                sintomas,
                id_paciente
            )

            cita = Cita(
                paciente,
                doctor,
                fecha,
                hora,
                id_cita
            )

            citas.append(cita)
        return citas
    except sqlite3.Error as e:
        print(f"Error al obtener las citas: {e}")
        return []
    finally:
        if conexion:
            conexion.close()

def obtener_citas_doctor(id_doctor):
    """
    Obtiene todas las citas de un doctor.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                fecha,
                hora
            FROM citas
            WHERE id_doctor = ?
        """, (id_doctor,))

        registros = cursor.fetchall()
        return registros
    except sqlite3.Error as e:
        print(f"Error al obtener las citas del doctor {id_doctor}: {e}")
        return []
    finally:
        if conexion:
            conexion.close()

def obtener_historial(nombre):
    """
    Obtiene el historial de un paciente.
    """
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT

                c.id_cita,
                c.fecha,
                c.hora,
                d.id_doctor,
                d.nombre,
                d.especialidad,
                p.id_paciente,
                p.nombre,
                p.sintomas

            FROM citas c
            INNER JOIN doctores d
                ON d.id_doctor = c.id_doctor
            INNER JOIN pacientes p
                ON p.id_paciente = c.id_paciente
            WHERE p.nombre LIKE ?
            ORDER BY c.fecha
        """, (f"%{nombre}%",))

        registros = cursor.fetchall()

        citas = []

        for (
            id_cita,
            fecha,
            hora,
            id_doctor,
            nombre_doctor,
            especialidad,
            id_paciente,
            nombre_paciente,
            sintomas
        ) in registros:
            doctor = Doctor(
                nombre_doctor,
                especialidad,
                id_doctor
            )

            paciente = Paciente(
                nombre_paciente,
                sintomas,
                id_paciente
            )

            cita = Cita(
                paciente,
                doctor,
                fecha,
                hora,
                id_cita
            )

            citas.append(cita)

        return citas
    except sqlite3.Error as e:
        print(f"Error al obtener el historial del paciente {nombre}: {e}")
        return []
    finally:
        if conexion:
            conexion.close()