# ============================================
# MODULO: computadora.py
# AUTOR: Lizardo Cordova
# DESCRIPCION: Gestiona la seleccion aleatoria
#              de la opcion por parte de la computadora.
# ============================================

import random
from datos import OPCIONES


def elegir_opcion():
    """
    La computadora selecciona una opcion al azar
    utilizando random.choice() sobre la tupla de opciones.
    Devuelve la opcion seleccionada como cadena de texto.
    """
    eleccion = random.choice(OPCIONES)
    return eleccion
