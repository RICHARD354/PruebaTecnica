def leer_entero(mensaje):
    """
    Solicita un número entero hasta que el usuario ingrese un valor válido.
    """
    while True:
        try:
            return int(input(mensaje))
        except ValueError:

            print("\nDebe ingresar un número.")

def leer_opcion(mensaje, minimo, maximo):
    """
    Solicita una opción dentro de un rango.
    """
    while True:
        opcion = leer_entero(mensaje)
        if minimo <= opcion <= maximo:
            return opcion
        print(f"\nDebe ingresar un número entre {minimo} y {maximo}.")