from servicios.hospital import Hospital
from menus import menu

def main():

    hospital = Hospital()

    while True:

        menu.mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("\nGracias por utilizar el sistema.")
            break

        elif opcion == "1":
            menu.registrar_doctor(hospital)
            menu.mostrar_doctores(hospital)
        elif opcion == "2":
            menu.registrar_paciente(hospital)
            menu.mostrar_pacientes(hospital)

        elif opcion == "3":
            menu.agendar_cita(hospital)

        elif opcion == "4":
            print("\n[Mostrar citas]")

        elif opcion == "5":
            print("\n[Buscar historial]")

        else:
            print("\nOpción no válida.")


if __name__ == "__main__":
    main()