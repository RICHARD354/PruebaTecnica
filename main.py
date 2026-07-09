from usuarios.persona import Persona

from usuarios.doctor import Doctor
from usuarios.paciente import Paciente


doctor = Doctor("Juan Pérez", "Cardiología")
paciente = Paciente("María López", "Dolor de cabeza")

print(doctor)
print(paciente)