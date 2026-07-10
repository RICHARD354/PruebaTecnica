from database import repositorio
from datetime import datetime

class Hospital:
    """
    Administra los doctores, pacientes y citas del sistema.
    """

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
        Registra una cita si se cumple con los requirimientos del hospital.
        """
        if not self.validar_fecha_hora_cita(cita.fecha, cita.hora):
            return "Fecha y hora no validos, fuera de tiempo."

        citas = repositorio.obtener_citas_doctor(
            cita.doctor.id_doctor
        )

        for fecha_existente, hora_existente in citas:
            if fecha_existente == cita.fecha and hora_existente == cita.hora:
                return "El doctor ya tiene una cita en ese horario."
        repositorio.guardar_cita(cita)
        return "Cita registrada correctamente."

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

    def validar_fecha_hora_cita(self, fecha, hora):
        """
        Verifica que la fecha y hora de la cita no sean anteriores
        a la fecha y hora actual.
        """
        try:
            fecha_hora_cita = datetime.strptime(
                f"{fecha} {hora}",
                "%d/%m/%Y %H:%M"
            )

            return fecha_hora_cita >= datetime.now()

        except ValueError:
            return False
