from usuarios.persona import Persona

class Paciente(Persona):
    """
    Representa a un paciente del hospital.
    """
    def __init__(self, nombre, sintomas, id_paciente=None):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.sintomas = sintomas

    def __str__(self):
        return (
            f"Paciente: {self.nombre} | "
            f"Síntomas: {self.sintomas}"
        )