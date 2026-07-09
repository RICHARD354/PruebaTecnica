class Cita:
    """
    Representa una cita médica entre un paciente y un doctor.
    """

    def __init__(self, paciente, doctor, fecha, hora):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return (
            f"Paciente: {self.paciente.nombre} | "
            f"Doctor: {self.doctor.nombre} ({self.doctor.especialidad}) | "
            f"Fecha: {self.fecha} | "
            f"Hora: {self.hora}"
        )