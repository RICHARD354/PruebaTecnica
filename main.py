from usuarios.doctor import Doctor
from usuarios.paciente import Paciente
from servicios.hospital import Hospital
from servicios.cita import Cita

hospital = Hospital()

doctor1 = Doctor("Juan Pérez", "Cardiología")
doctor2 = Doctor("Ana Torres", "Pediatría")

hospital.registrar_doctor(doctor1)
hospital.registrar_doctor(doctor2)

paciente1 = Paciente("Carlos Gómez", "Dolor de cabeza")
paciente2 = Paciente("Laura Díaz", "Fiebre")

hospital.registrar_paciente(paciente1)
hospital.registrar_paciente(paciente2)

print("--- DOCTORES ---")
for doctor in hospital.doctores:
    print(doctor)

print()

print("--- PACIENTES ---")
for paciente in hospital.pacientes:
    print(paciente)


cita1 = Cita(
    paciente1,
    doctor1,
    "10/07/2026",
    "10:00"
)

hospital.registrar_cita(cita1)

print("\n--- CITAS ---")

for cita in hospital.citas:
    print(cita)

cita2 = Cita(
    paciente2,
    doctor1,
    "10/07/2026",
    "10:00"
)

if hospital.registrar_cita(cita2):
    print("Cita registrada correctamente.")
else:
    print("Error: el doctor ya tiene una cita en ese horario.")


cita3 = Cita(
    paciente1,
    doctor2,
    "20/07/2026",
    "13:00"
)
hospital.registrar_cita(cita3)

cita4 = Cita(
    paciente1,
    doctor2,
    "25/07/2026",
    "13:00"
)
hospital.registrar_cita(cita4)


print("\n--- HISTORIAL ---")

historial = hospital.buscar_historial("Carlos Gómez")

for cita in historial:
    print(cita)