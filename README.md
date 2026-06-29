# Piedra, Papel o Tijera

Proyecto de programacion desarrollado en Python como parte de la materia Logica de Programacion 1, en la Universidad Internacional del Ecuador (UIDE).

---

## Integrantes

- Lizardo Cordova

## Objetivo del sistema

El objetivo de este proyecto es implementar un juego de Piedra, Papel o Tijera en el que el usuario compite contra la computadora. El desarrollo integra los contenidos trabajados a lo largo de las cuatro unidades de la materia, con enfasis en la correcta aplicacion de estructuras logicas, manejo de datos y organizacion modular del codigo.

El programa esta disenado para ejecutarse desde la consola, con una interfaz de texto clara que guia al usuario en cada paso del juego.

## Descripcion de funcionalidades

El sistema cuenta con las siguientes funcionalidades:

- Juego por rondas: el usuario ingresa su eleccion y la computadora selecciona una opcion al azar. Gana la partida quien alcance primero tres rondas ganadas.
- Validacion de entrada: si el usuario ingresa una opcion incorrecta, el sistema lo notifica y solicita nuevamente la eleccion hasta recibir un valor valido.
- Sistema de puntaje: el programa lleva el conteo de victorias del usuario, de la computadora y de los empates durante cada partida.
- Historial de jugadas: cada ronda se registra en una estructura de datos para su posterior analisis.
- Estadisticas finales: al concluir la partida se presenta el total de rondas jugadas, la frecuencia de uso de cada opcion, la opcion mas utilizada por el usuario y el porcentaje de victorias.
- Partidas multiples: al finalizar cada partida, el sistema consulta al usuario si desea iniciar una nueva.

## Estructura del proyecto

El codigo esta organizado en modulos independientes, cada uno con una responsabilidad especifica:

| Archivo           | Descripcion                                                   |
|-------------------|---------------------------------------------------------------|
| main.py           | Archivo principal. Coordina la ejecucion del programa.        |
| datos.py          | Define las constantes del juego: opciones, emojis y reglas.   |
| jugador.py        | Gestiona la entrada del usuario y su validacion.              |
| computadora.py    | Genera la eleccion aleatoria de la computadora.               |
| logica.py         | Determina el resultado de cada ronda.                         |
| puntaje.py        | Administra el marcador y el historial de rondas.              |
| estadisticas.py   | Calcula y presenta las estadisticas al finalizar la partida.  |

## Conceptos de programacion aplicados

- Manejo de datos: variables y constantes con nombres descriptivos.
- Tuplas: para almacenar las opciones del juego, al ser valores que no se modifican.
- Listas: para registrar el historial de rondas durante la partida.
- Diccionarios: para el marcador, las reglas del juego y los simbolos visuales.
- Condicionales (if / elif / else): para determinar el resultado de cada ronda y gestionar el flujo del programa.
- Operadores relacionales: == , > , >= aplicados en comparaciones de valores.
- Operadores logicos: or utilizado en la validacion de respuestas del usuario.
- Bucle while: para el control del juego por rondas y la validacion de entradas.
- Bucle for: para recorrer las opciones disponibles y el historial de jugadas.
- Funciones: el programa esta completamente dividido en funciones con una unica responsabilidad.
- Algoritmos: calculo de la opcion mas frecuente y del porcentaje de victorias sobre el total de rondas.

## Relacion con el impacto tecnologico

Este proyecto, si bien es de caracter academico, refleja principios de diseno de software aplicados en sistemas reales: separacion de responsabilidades, reutilizacion de codigo y trazabilidad de datos. La capacidad de estructurar un programa en modulos independientes es una practica fundamental en el desarrollo de software profesional, y su comprension desde etapas tempranas de formacion contribuye a una base solida para proyectos de mayor complejidad.

## Instrucciones de ejecucion

1. Tener instalado Python 3 en el equipo.
2. Descargar todos los archivos del proyecto en una misma carpeta.
3. Abrir la terminal en esa carpeta.
4. Ejecutar el siguiente comando:

    python main.py

5. Seguir las instrucciones en pantalla escribiendo: piedra, papel o tijera.

## Fecha

Junio 2026

---

Proyecto academico - Universidad Internacional del Ecuador (UIDE) - Logica de Programacion 1
