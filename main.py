# ============================================
# PROYECTO: Piedra, Papel o Tijera
# ARCHIVO: main.py
# AUTOR: Lizardo Cordova
# MATERIA: Logica de Programacion 1
# UNIVERSIDAD: Universidad Internacional del Ecuador
# FECHA: Junio 2026
# ============================================
# Archivo principal del programa. Desde aqui se
# coordina la ejecucion del juego importando las
# funciones definidas en los demas modulos.
# ============================================

from datos import RONDAS_PARA_GANAR
import jugador
import computadora
import logica
import puntaje
import estadisticas


def mostrar_bienvenida():
    """Presenta el titulo del juego al iniciar el programa."""
    print("=" * 40)
    print("     PIEDRA, PAPEL O TIJERA")
    print("=" * 40)
    print(f"Gana quien llegue primero a {RONDAS_PARA_GANAR} rondas.")


def mostrar_ganador_final(ganador, marcador):
    """Muestra el resultado final de la partida."""
    print("\n" + "=" * 40)
    if ganador == "jugador":
        print("   FELICIDADES, GANO EL JUGADOR.")
    else:
        print("   GANO LA COMPUTADORA.")
    print(f"   Marcador final: Jugador {marcador['jugador']} - {marcador['computadora']} Computadora")
    print("=" * 40)


def jugar_partida():
    """
    Ejecuta una partida completa, ronda por ronda,
    hasta que alguno de los participantes alcance
    el numero de victorias necesarias para ganar.
    """
    # Se inicializa el marcador como diccionario y el historial como lista
    marcador = puntaje.crear_marcador()
    historial = []

    # El bucle continua mientras no exista un ganador final
    while puntaje.hay_ganador_final(marcador) is None:

        # Paso 1: el jugador selecciona su opcion
        eleccion_jugador = jugador.pedir_opcion()

        # Paso 2: la computadora selecciona su opcion al azar
        eleccion_pc = computadora.elegir_opcion()

        # Paso 3: se determina el resultado de la ronda
        resultado = logica.determinar_ganador(eleccion_jugador, eleccion_pc)
        logica.mostrar_resultado_ronda(resultado)

        # Paso 4: se actualiza el marcador y se registra la ronda
        puntaje.actualizar_marcador(marcador, resultado)
        puntaje.registrar_ronda(historial, eleccion_jugador, eleccion_pc, resultado)

        # Paso 5: se muestra el puntaje actualizado
        puntaje.mostrar_marcador(marcador)

    # Al salir del bucle, se identifica y muestra al ganador
    ganador = puntaje.hay_ganador_final(marcador)
    mostrar_ganador_final(ganador, marcador)

    # Se presentan las estadisticas de la partida
    estadisticas.mostrar_estadisticas(historial, marcador)


def main():
    """Funcion principal que controla el flujo completo del programa."""
    mostrar_bienvenida()

    # El programa permite jugar multiples partidas consecutivas
    seguir = True
    while seguir:
        jugar_partida()
        seguir = jugador.preguntar_si_continuar()

    print("\nGracias por utilizar el programa.")


# El programa se ejecuta unicamente si se llama este archivo directamente
if __name__ == "__main__":
    main()
