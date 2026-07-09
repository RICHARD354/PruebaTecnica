class Persona:
    """
    Clase Padre para representar una persona dentro del hospital.
    """
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre