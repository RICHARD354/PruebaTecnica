from usuarios.doctor import Doctor
from usuarios.paciente import Paciente
from servicios.cita import Cita
from utilidades.validaciones import leer_opcion
from utilidades.validaciones import leer_texto
from utilidades.validaciones import leer_fecha
from utilidades.validaciones import leer_hora

def mostrar_menu():
    """Muestra el menú principal."""

    print("\n" + "-" * 45)
    print("      SISTEMA DE GESTIÓN HOSPITALARIA")
    print("-" * 45)
    print("1. Registrar doctor")
    print("2. Registrar paciente")
    print("3. Agendar cita")
    print("4. Mostrar citas")
    print("5. Buscar historial de paciente")
    print("0. Salir")
    print("-" * 45)

def registrar_doctor(hospital):
    """Solicita la información y registra un doctor."""

    print("\n--- Registrar Doctor ---")

    nombre = leer_texto("Nombre: ")
    especialidad = leer_texto("Especialidad: ")
    
    doctor = Doctor(nombre, especialidad)
    hospital.registrar_doctor(doctor)

    print("\nDoctor registrado correctamente.")

def mostrar_doctores(hospital):
    """Muestra todos los doctores registrados."""
    print("\n--- Doctores Registrados ---")
    doctores = hospital.obtener_doctores()

    if not doctores:
        print("No hay doctores registrados.")
        return

    for indice, doctor in enumerate(doctores, start=1):
        print(f"{indice}. {doctor}")

def registrar_paciente(hospital):
    """
    Solicita los datos del paciente y lo registra.
    """
    print("\n--- Registrar Paciente ---")

    nombre = leer_texto("Nombre: ")
    motivo = leer_texto("Síntomas/Motivo: ")

    paciente = Paciente(nombre, motivo)
    hospital.registrar_paciente(paciente)

    print("\nPaciente registrado correctamente.")

def mostrar_pacientes(hospital):
    """
    Muestra todos los pacientes registrados.
    """
    print("\n--- Pacientes Registrados ---")
    pacientes = hospital.obtener_pacientes()

    if not pacientes:
        print("No hay pacientes registrados.")
        return

    for indice, paciente in enumerate(pacientes, start=1):
        print(f"{indice}. {paciente}")

def agendar_cita(hospital):

    print("\n--- Agendar Cita ---")

    doctores = hospital.obtener_doctores()

    if not doctores:
        print("No hay doctores registrados.")
        return

    pacientes = hospital.obtener_pacientes()

    if not pacientes:
        print("No hay pacientes registrados.")
        return

    print("\nDoctores disponibles:")

    for i, doctor in enumerate(doctores, start=1):
        print(f"{i}. {doctor}")

    opcion_doctor = leer_opcion(
        "\nSeleccione un doctor: ",
        1,
        len(doctores)
    ) - 1
    doctor = doctores[opcion_doctor]

    print("\n Pacientes registrados:")

    for i, paciente in enumerate(pacientes, start=1):
        print(f"{i}. {paciente}")

    opcion_paciente = leer_opcion(
        "\nSeleccione un paciente: ",
        1,
        len(doctores)
    ) - 1
    paciente = pacientes[opcion_paciente]

    fecha = leer_fecha("Fecha (dd/mm/aaaa): ")
    hora = leer_hora("Hora (HH:MM): ")

    cita = Cita(
        paciente,
        doctor,
        fecha,
        hora
    )

    if hospital.registrar_cita(cita):
        print("\nCita registrada correctamente.")

    else:
        print("\nEl doctor ya tiene una cita en ese horario.")

def mostrar_citas(hospital):
    """
    Muestra todas las citas registradas.
    """
    print("\n--- Citas Programadas ---")

    citas = hospital.obtener_citas()

    if not citas:
        print("No hay citas registradas.")
        return

    for i, cita in enumerate(citas, start=1):
        print(f"{i}. {cita}")

def buscar_historial(hospital):
    """
    Busca el historial de citas de un paciente.
    """

    print("\n--- Historial del Paciente ---")
    nombre = input("Nombre del paciente: ").strip()
    historial = hospital.buscar_historial(nombre)

    if not historial:
        print("\nNo se encontraron citas para ese paciente.")
        return

    for i, cita in enumerate(historial, start=1):
        print(f"{i}. {cita}")