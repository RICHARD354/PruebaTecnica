from servicios.hospital import Hospital
from menus import menu
from utilidades.validaciones import leer_opcion

def main():

    hospital = Hospital()

    while True:

        menu.mostrar_menu()

        opcion = leer_opcion(
            "Seleccione una opción: ",
            0,
            5
        )

        if opcion == 0:
            print("\nGracias por utilizar el sistema.")
            break

        elif opcion == 1:
            menu.registrar_doctor(hospital)
            menu.mostrar_doctores(hospital)
        elif opcion == 2:
            menu.registrar_paciente(hospital)
            menu.mostrar_pacientes(hospital)

        elif opcion == 3:
            menu.agendar_cita(hospital)

        elif opcion == 4:
            menu.mostrar_citas(hospital)

        elif opcion == 5:
            menu.buscar_historial(hospital)

        else:
            print("\nOpción no válida.")


if __name__ == "__main__":
    main()