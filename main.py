from usuarios.doctor import Doctor
from usuarios.paciente import Paciente
from servicios.cita import Cita


doctor = Doctor("Juan Pérez", "Cardiología")
paciente = Paciente("María López", "Dolor de cabeza")

cita = Cita(
    paciente,
    doctor,
    "10/07/2026",
    "10:00"
)

print(cita)