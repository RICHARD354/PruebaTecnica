from usuarios.persona import Persona

class Doctor(Persona):
    """
    Representa a un doctor del hospital.
    """

    def __init__(self, nombre, especialidad):
        super().__init__(nombre)
        self.especialidad = especialidad

    def __str__(self):
        return f"Doctor: {self.nombre} | Especialidad: {self.especialidad}"