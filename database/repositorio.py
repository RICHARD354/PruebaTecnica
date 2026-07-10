from database.conexion import obtener_conexion

def guardar_doctor(doctor):
    """
    Guarda un doctor en la base de datos.
    """
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

    conexion.commit()
    conexion.close()

def guardar_paciente(paciente):
    """
    Guarda un paciente en la base de datos.
    """
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

    conexion.commit()
    conexion.close()

def guardar_cita(cita):
    """
    Guarda una cita en la base de datos.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO citas(
            paciente,
            doctor,
            especialidad,
            fecha,
            hora
        )
        VALUES(?, ?, ?, ?, ?)
        """,
        (
            cita.paciente.nombre,
            cita.doctor.nombre,
            cita.doctor.especialidad,
            cita.fecha,
            cita.hora
        )
    )

    conexion.commit()
    conexion.close()