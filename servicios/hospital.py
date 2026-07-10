class Hospital:
    """
    Administra los doctores, pacientes y citas del sistema.
    """

    def __init__(self):
        self.doctores = []
        self.pacientes = []
        self.citas = []

    def registrar_doctor(self, doctor):
        """
        Agrega un doctor al sistema.
        """
        self.doctores.append(doctor)

    def registrar_paciente(self, paciente):
        """
        Agrega un paciente al sistema.
        """
        self.pacientes.append(paciente)

    def registrar_cita(self, cita):

        """
        Registra una cita si el doctor está disponible.
        """

        for cita_existente in self.citas:

            if (
                cita_existente.doctor == cita.doctor
                and cita_existente.fecha == cita.fecha
                and cita_existente.hora == cita.hora
            ):
                return False

        self.citas.append(cita)
        return True

    def obtener_doctores(self):
        """
        Devuelve la lista de doctores registrados.
        """
        return self.doctores

    def obtener_pacientes(self):
        """
        Devuelve la lista de pacientes registrados.
        """
        return self.pacientes
    
    def obtener_citas(self):
        """
        Devuelve la lista de citas registradas.
        """
        return self.citas
    
    def buscar_historial(self, nombre_paciente):
        """
        Devuelve todas las citas de un paciente.
        """

        historial = []

        for cita in self.citas:

            if cita.paciente.nombre.lower() == nombre_paciente.lower():
                historial.append(cita)

        return historial

    def obtener_doctor(self, indice):
        """
        Devuelve un doctor según su posición en la lista.
        """
        return self.doctores[indice]


    def obtener_paciente(self, indice):
        """
        Devuelve un paciente según su posición en la lista.
        """
        return self.pacientes[indice]