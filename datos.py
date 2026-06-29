# ============================================
# MODULO: datos.py
# AUTOR: Lizardo Cordova
# DESCRIPCION: Define los datos fijos del programa:
#              las opciones validas, los simbolos
#              visuales y las reglas del juego.
# ============================================

# Se utiliza una TUPLA para las opciones del juego.
# Se eligio una tupla porque sus valores no cambian
# en ningun momento durante la ejecucion.
OPCIONES = ("piedra", "papel", "tijera")

# DICCIONARIO que asocia cada opcion con su simbolo visual.
# Estructura: clave = opcion, valor = simbolo.
SIMBOLOS = {
    "piedra": "[PIEDRA]",
    "papel":  "[PAPEL]",
    "tijera": "[TIJERA]"
}

# DICCIONARIO que define las reglas del juego.
# Cada clave representa una opcion y su valor
# es la opcion a la que le gana.
# Ejemplo: piedra le gana a tijera.
REGLAS = {
    "piedra": "tijera",
    "papel":  "piedra",
    "tijera": "papel"
}

# Numero de rondas necesarias para ganar la partida completa.
RONDAS_PARA_GANAR = 3
