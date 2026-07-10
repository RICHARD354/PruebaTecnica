from usuarios.persona import Persona

class Doctor(Persona):
    """
    Representa a un doctor del hospital.
    """

    def __init__(self, nombre, especialidad, id_doctor=None):
        self.id_doctor = id_doctor
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return (
            f"Doctor: {self.nombre} | "
            f"Especialidad: {self.especialidad}"
        )