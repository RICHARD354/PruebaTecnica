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
        Registra una cita médica.
        """
        self.citas.append(cita)

