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

print()
print("=== CITAS ===")

for cita in hospital.citas:
    print(cita)