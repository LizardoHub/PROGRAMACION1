# ============================================
# MODULO: jugador.py
# AUTOR: Lizardo Cordova
# DESCRIPCION: Gestiona la entrada del usuario
#              y valida que sea una opcion correcta.
# ============================================

from datos import OPCIONES, SIMBOLOS


def pedir_opcion():
    """
    Solicita al usuario que ingrese su eleccion.
    Utiliza un bucle while para repetir la solicitud
    en caso de que la entrada no sea valida.
    """
    while True:
        print("\nOpciones disponibles:")

        # Bucle for con enumerate para mostrar las opciones numeradas.
        # enumerate() devuelve el indice y el valor de cada elemento.
        for numero, opcion in enumerate(OPCIONES, start=1):
            print(f"  {numero}. {SIMBOLOS[opcion]}  {opcion}")

        eleccion = input("Ingrese su eleccion: ").lower().strip()

        # Condicional: se verifica si la entrada existe en la tupla de opciones.
        # El operador "in" permite comprobar si un valor pertenece a una secuencia.
        if eleccion in OPCIONES:
            return eleccion
        else:
            print("La opcion ingresada no es valida. Intente nuevamente.")


def preguntar_si_continuar():
    """
    Consulta al usuario si desea iniciar una nueva partida.
    Devuelve True si responde afirmativamente, False en caso contrario.
    """
    while True:
        respuesta = input("\nDesea jugar otra partida? (si/no): ").lower().strip()

        # Operador logico OR: acepta tanto "si" como "s" como respuesta afirmativa
        if respuesta == "si" or respuesta == "s":
            return True
        elif respuesta == "no" or respuesta == "n":
            return False
        else:
            print("Por favor responda 'si' o 'no'.")
