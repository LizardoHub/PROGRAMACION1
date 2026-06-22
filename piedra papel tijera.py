# ============================================
# PROYECTO: Juego Piedra, Papel o Tijera
# AUTOR: Lizardo Cordova
# FECHA: Junio 2026
# DESCRIPCION: Juego de 1 jugador contra la computadora
# ESTADO: Avance - funcionalidades basicas implementadas
# PENDIENTE: sistema de rondas, puntaje final, repetir partida
# ============================================

# Importamos random para que la computadora elija al azar
import random

# Opciones que puede elegir cualquier jugador
opciones_validas = ["piedra", "papel", "tijera"]


# ============================================
# FUNCION: mostrar_bienvenida
# Solo imprime el titulo del juego
# ============================================
def mostrar_bienvenida():
    print("==============================")
    print("   PIEDRA, PAPEL O TIJERA")
    print("==============================")
    print()


# ============================================
# FUNCION: pedir_eleccion_jugador
# Le pide al usuario que escriba su eleccion
# Si escribe algo incorrecto, se lo vuelve a pedir (bucle)
# ============================================
def pedir_eleccion_jugador():
    while True:
        print("Tus opciones son: piedra, papel, tijera")
        eleccion = input("Que eliges?: ").lower()

        # Condicional: verifica si lo que escribio es valido
        if eleccion in opciones_validas:
            return eleccion
        else:
            print("Eso no es una opcion valida, intenta de nuevo.")
            print()


# ============================================
# FUNCION: eleccion_computadora
# La computadora escoge una opcion al azar
# ============================================
def eleccion_computadora():
    return random.choice(opciones_validas)


# ============================================
# FUNCION: determinar_resultado
# Compara lo que eligio cada uno y dice quien gano
# PENDIENTE: conectar con sistema de puntaje
# ============================================
def determinar_resultado(jugador, computadora):
    print(f"Tu elegiste:           {jugador}")
    print(f"La computadora eligio: {computadora}")
    print()

    # Condicional: primero revisamos si hay empate
    if jugador == computadora:
        print("Es un EMPATE.")

    # Condicional: casos en que el jugador gana
    elif (jugador == "piedra"  and computadora == "tijera") or \
         (jugador == "papel"   and computadora == "piedra") or \
         (jugador == "tijera"  and computadora == "papel"):
        print("GANASTE esta ronda!")

    # Si no empataron y el jugador no gano, perdio
    else:
        print("Perdiste esta ronda.")


# ============================================
# FUNCION: puntaje_final  (PENDIENTE)
# Esta funcion todavia no esta implementada
# Se agregara en la siguiente entrega
# ============================================
def puntaje_final():
    # TODO: llevar conteo de victorias por ronda
    # TODO: mostrar quien gano la partida completa
    print()
    print("--- Puntaje final ---")
    print("(Esta seccion esta pendiente de implementar)")
    print("---------------------")


# ============================================
# PROGRAMA PRINCIPAL
# ============================================
mostrar_bienvenida()

# Pedimos la eleccion del jugador
eleccion_jugador = pedir_eleccion_jugador()

# La computadora elige
eleccion_pc = eleccion_computadora()

# Mostramos el resultado de esta ronda
print()
determinar_resultado(eleccion_jugador, eleccion_pc)

# Llamamos al puntaje final (pendiente)
puntaje_final()

print()
print("Gracias por jugar!")
# PENDIENTE: agregar opcion para jugar varias rondas seguidas
