# ============================================
# MODULO: puntaje.py
# AUTOR: Lizardo Cordova
# DESCRIPCION: Administra el marcador de la partida
#              y el historial de rondas jugadas.
# ============================================

from datos import RONDAS_PARA_GANAR


def crear_marcador():
    """
    Genera un diccionario nuevo para llevar el puntaje.
    Se llama al inicio de cada partida.
    """
    marcador = {
        "jugador":      0,
        "computadora":  0,
        "empates":      0
    }
    return marcador


def actualizar_marcador(marcador, resultado):
    """
    Incrementa en uno el puntaje del ganador de la ronda.
    Recibe el diccionario marcador y el resultado obtenido.
    """
    if resultado == "jugador":
        marcador["jugador"] += 1
    elif resultado == "computadora":
        marcador["computadora"] += 1
    else:
        marcador["empates"] += 1


def mostrar_marcador(marcador):
    """
    Presenta el puntaje actualizado de la partida en curso.
    """
    print("\n--- Puntaje actual ---")
    print(f"  Jugador:      {marcador['jugador']}")
    print(f"  Computadora:  {marcador['computadora']}")
    print(f"  Empates:      {marcador['empates']}")
    print("----------------------")


def hay_ganador_final(marcador):
    """
    Verifica si alguno de los participantes alcanzo
    el numero de victorias requeridas para ganar la partida.
    Devuelve el nombre del ganador o None si la partida continua.
    """
    # Operador relacional >= (mayor o igual que)
    if marcador["jugador"] >= RONDAS_PARA_GANAR:
        return "jugador"
    elif marcador["computadora"] >= RONDAS_PARA_GANAR:
        return "computadora"
    else:
        return None


def registrar_ronda(historial, jugador, computadora, resultado):
    """
    Almacena los datos de una ronda en el historial.
    El historial es una lista y cada ronda se guarda como una tupla.
    """
    # Se crea una tupla con los tres datos de la ronda
    ronda = (jugador, computadora, resultado)
    # Se agrega la tupla al final de la lista historial
    historial.append(ronda)
