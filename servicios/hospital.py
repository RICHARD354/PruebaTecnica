from database import repositorio

class Hospital:
    """
    Administra los doctores, pacientes y citas del sistema.
    """
    pass

    def registrar_doctor(self, doctor):
        """
        Agrega un doctor al sistema.
        """
        repositorio.guardar_doctor(doctor)

    def registrar_paciente(self, paciente):
        """
        Agrega un paciente al sistema.
        """
        repositorio.guardar_paciente(paciente)

    def registrar_cita(self, cita):
        """
        Registra una cita si el doctor está disponible.
        """
        citas = repositorio.obtener_citas_doctor(
            cita.doctor.id_doctor
        )

        for fecha, hora in citas:
            if (
                fecha == cita.fecha
                and hora == cita.hora
            ):
                return False

        repositorio.guardar_cita(cita)
        return True

    def obtener_doctores(self):
        """
        Devuelve la lista de doctores registrados.
        """
        return repositorio.obtener_doctores()

    def obtener_pacientes(self):
        """
        Devuelve la lista de pacientes registrados.
        """
        return repositorio.obtener_pacientes()
    
    def obtener_citas(self):
        """
        Devuelve la lista de citas registradas.
        """
        return repositorio.obtener_citas()
    
    def buscar_historial(self, nombre_paciente):
        """
        Devuelve todas las citas de un paciente.
        """
        return repositorio.obtener_historial(nombre_paciente)
