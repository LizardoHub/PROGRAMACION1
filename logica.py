# ============================================
# MODULO: logica.py
# AUTOR: Lizardo Cordova
# DESCRIPCION: Contiene las reglas que determinan
#              el resultado de cada ronda del juego.
# ============================================

from datos import REGLAS, SIMBOLOS


def determinar_ganador(eleccion_jugador, eleccion_computadora):
    """
    Compara las dos elecciones y determina el resultado.
    Devuelve: "empate", "jugador" o "computadora".
    """
    print(f"\nJugador eligio:       {SIMBOLOS[eleccion_jugador]}  {eleccion_jugador}")
    print(f"Computadora eligio:   {SIMBOLOS[eleccion_computadora]}  {eleccion_computadora}")

    # Condicional 1: ambas elecciones son iguales, resultado empate.
    # Se utiliza el operador relacional == (igualdad).
    if eleccion_jugador == eleccion_computadora:
        return "empate"

    # Condicional 2: se consulta en el diccionario REGLAS si la eleccion
    # del jugador le gana a la de la computadora.
    # Se utiliza == para comparar el valor obtenido del diccionario.
    elif REGLAS[eleccion_jugador] == eleccion_computadora:
        return "jugador"

    # Condicional 3: si no hubo empate ni victoria del jugador,
    # la computadora es la ganadora de la ronda.
    else:
        return "computadora"


def mostrar_resultado_ronda(resultado):
    """
    Presenta en pantalla el resultado de la ronda actual.
    """
    if resultado == "empate":
        print("Resultado: EMPATE")
    elif resultado == "jugador":
        print("Resultado: EL JUGADOR GANO ESTA RONDA")
    else:
        print("Resultado: LA COMPUTADORA GANO ESTA RONDA")
