from usuarios.persona import Persona

class Paciente(Persona):
    """
    Representa a un paciente del hospital.
    """
    def __init__(self, nombre, sintomas):
        super().__init__(nombre)
        self.sintomas = sintomas

    def __str__(self):
        return f"Paciente: {self.nombre} | Síntomas: {self.sintomas}"