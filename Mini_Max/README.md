# Algoritmo Minimax — Tres en Raya

## Descripción del Algoritmo

Minimax es un algoritmo de toma de decisiones utilizado en inteligencia artificial para juegos de dos jugadores de suma cero. El algoritmo asume que ambos jugadores actúan de forma **óptima**: uno busca maximizar su puntuación (jugador MAX) y el otro busca minimizarla (jugador MIN).

El funcionamiento se basa en la construcción recursiva de un **árbol de juego**, evaluando todos los estados posibles hasta alcanzar un estado terminal (victoria, derrota o empate):

- `+1` → gana X (MAX)
- `-1` → gana O (MIN)
- `0`  → empate

En esta implementación, **X representa al jugador MAX** y **O al jugador MIN**. La función `ai_play` detecta automáticamente de quién es el turno y devuelve el movimiento óptimo para ese jugador. La partida es **IA vs IA**: ambos lados juegan con Minimax, por lo que el resultado siempre será un empate con juego perfecto.

### Funciones principales

| Función | Descripción |
|---------|-------------|
| `max_value(board)` | Retorna el valor máximo alcanzable desde el estado actual (turno de X) |
| `min_value(board)` | Retorna el valor mínimo alcanzable desde el estado actual (turno de O) |
| `ai_play(board)` | Retorna la acción óptima para el jugador en turno |
| `players(board)` | Determina de quién es el turno según el estado del tablero |
| `terminal(board)` | Verifica si el juego terminó (victoria o empate) |
| `utility(board)` | Retorna el valor numérico del estado terminal (+1, -1 o 0) |

---

## Requisitos de Instalación

### 1. Python

Verificar que Python esté instalado:

```bash
python --version
```

Si no está instalado, descargarlo desde [https://www.python.org](https://www.python.org).

### 2. Flask

Instalar Flask desde la terminal del sistema (cmd, PowerShell o Terminal):

```bash
pip install flask
```

Verificar la instalación:

```bash
flask --version
```

---

## Estructura de Archivos

```
Minimax/
├── app.py              ← Servidor Flask, simula la partida completa
├── minimax.py          ← Implementación de min_value, max_value y ai_play
├── utils.py            ← Funciones auxiliares: terminal, utility, result, actions, players
└── templates/
    └── index.html      ← Interfaz visual del juego
```

> **Importante:** La carpeta `templates` debe estar en el mismo directorio que `app.py`. Flask no encontrará el HTML si no respeta esta estructura.

---

## Instrucciones de Ejecución


1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar el servidor:

```bash
python app.py
```

3. Abrir un navegador web y acceder a:

```
http://127.0.0.1:5000
```

4. Presionar el botón **SIMULAR PARTIDA** para ver cómo Minimax juega ambos lados de forma óptima. Se puede ajustar la velocidad de animación con el control deslizante.

## Detener el Servidor

Presionar `Ctrl + C` en la terminal donde se está ejecutando `app.py`.
