# ============================================
# MODULO: estadisticas.py
# AUTOR: Lizardo Cordova
# DESCRIPCION: Realiza calculos sobre el historial
#              de rondas y presenta las estadisticas
#              al finalizar la partida.
# ============================================


def contar_jugadas(historial):
    """
    Contabiliza cuantas veces el jugador utilizo
    cada opcion durante la partida.
    Devuelve un diccionario con el conteo por opcion.
    """
    conteo = {"piedra": 0, "papel": 0, "tijera": 0}

    # Bucle for que recorre cada elemento de la lista historial.
    # Cada ronda es una tupla: (jugador, computadora, resultado).
    for ronda in historial:
        # Se extrae el primer elemento de la tupla (eleccion del jugador)
        eleccion_jugador = ronda[0]
        conteo[eleccion_jugador] += 1

    return conteo


def opcion_mas_usada(conteo):
    """
    Algoritmo que identifica la opcion utilizada
    con mayor frecuencia por el jugador.
    Devuelve la opcion y la cantidad de veces que se uso.
    """
    opcion_mayor = ""
    cantidad_mayor = -1

    # Bucle for sobre el diccionario usando .items()
    # para obtener clave y valor al mismo tiempo.
    for opcion, cantidad in conteo.items():
        # Operador relacional > (mayor que)
        if cantidad > cantidad_mayor:
            cantidad_mayor = cantidad
            opcion_mayor = opcion

    return opcion_mayor, cantidad_mayor


def calcular_porcentaje_victorias(marcador, total_rondas):
    """
    Calcula el porcentaje de rondas ganadas por el jugador
    sobre el total de rondas disputadas.
    """
    # Condicional para evitar division entre cero
    if total_rondas == 0:
        return 0.0

    porcentaje = (marcador["jugador"] / total_rondas) * 100
    return round(porcentaje, 1)


def mostrar_estadisticas(historial, marcador):
    """
    Consolida y presenta todas las estadisticas
    al concluir la partida.
    """
    print("\n========== ESTADISTICAS DE LA PARTIDA ==========")

    total_rondas = len(historial)
    print(f"Total de rondas jugadas: {total_rondas}")

    # Solo se calculan estadisticas si se jugo al menos una ronda
    if total_rondas > 0:
        conteo = contar_jugadas(historial)

        print("\nFrecuencia de uso por opcion:")
        for opcion, cantidad in conteo.items():
            print(f"  {opcion}: {cantidad} vez/veces")

        favorita, veces = opcion_mas_usada(conteo)
        print(f"\nOpcion mas utilizada: {favorita} ({veces} vez/veces)")

        porcentaje = calcular_porcentaje_victorias(marcador, total_rondas)
        print(f"Porcentaje de victorias: {porcentaje}%")

    print("=================================================")
