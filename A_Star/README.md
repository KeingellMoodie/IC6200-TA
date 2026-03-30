# Algoritmo A* 

## Descripción del Algoritmo

El algoritmo A* (A estrella) es un algoritmo de búsqueda informada que encuentra el camino óptimo entre un nodo de inicio y un nodo de destino dentro de un grafo o, en este caso, una matriz bidimensional. A diferencia de algoritmos como BFS o DFS, A* utiliza una **función heurística** para guiar la búsqueda de forma más eficiente, priorizando los nodos que tienen mayor probabilidad de conducir al destino.

La función de evaluación es: `f(n) = g(n) + h(n)`, donde:

- `g(n)` es el costo acumulado desde el nodo inicial hasta el nodo actual.
- `h(n)` es la heurística estimada desde el nodo actual hasta el destino. En esta implementación se utiliza la **distancia Manhattan**.
- `f(n)` es el costo total estimado del camino que pasa por el nodo `n`.

A* garantiza encontrar el camino óptimo siempre que la heurística sea posible de implementar. La distancia Manhattan cumple esta condición en grillas (Cuadriculas) donde solo se permiten movimientos en cuatro direcciones.

La matriz utilizada representa:

| Valor | Significado |
|-------|-------------|
| `0`   | Celda vacía (transitable) |
| `1`   | Pared (no transitable) |
| `2`   | Nodo de inicio |
| `3`   | Nodo de destino |

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
A_Star/
├── app.py              ← Servidor Flask y lógica principal
├── astar.py            ← Implementación del algoritmo A*
└── templates/
    └── index.html      ← Interfaz visual
```

> **Importante:** La carpeta `templates` debe estar en el mismo directorio que `app.py`. Flask no encontrará el HTML si no respeta esta estructura.

---

## Instrucciones de Ejecución

### Con interfaz visual 

1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar el servidor:

```bash
python app.py
```

3. Abrir un navegador web y acceder a:

```
http://127.0.0.1:5000
```

4. Presionar el botón **INICIAR** para visualizar la ejecución del algoritmo paso a paso.

## Detener el Servidor

Presionar `Ctrl + C` en la terminal donde se está ejecutando `app.py`.
