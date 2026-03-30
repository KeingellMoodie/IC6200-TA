# Algoritmo de Dijkstra

## Descripción del Algoritmo

El algoritmo de Dijkstra es un algoritmo de búsqueda de caminos mínimos en grafos con pesos no negativos, propuesto por el científico Edsger W. Dijkstra en 1956. A diferencia de BFS, Dijkstra considera el **costo acumulado** de cada camino para determinar cuál explorar a continuación, garantizando encontrar siempre la ruta de menor costo total.

En esta implementación, Dijkstra opera sobre una **matriz bidimensional** donde cada movimiento entre celdas adyacentes tiene un costo uniforme de 1. El algoritmo utiliza una **cola de prioridad (min-heap)** que ordena los nodos por su costo acumulado, extrayendo siempre el de menor costo.

Características principales:

- **Completo:** siempre encuentra una solución si existe.
- **Óptimo:** garantiza el camino de menor costo total, incluso en grafos con pesos variables.
- **Relación con A\*:** Dijkstra puede verse como un caso especial de A* donde la heurística `h(n) = 0`. Esto significa que A* es más eficiente en la práctica cuando se cuenta con una buena heurística, mientras que Dijkstra explora el espacio de forma más exhaustiva.

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
Dijkstra/
├── app.py              ← Servidor Flask y lógica principal
├── dijkstra.py         ← Implementación del algoritmo de Dijkstra
└── templates/
    └── index.html      ← Interfaz visual
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

4. Presionar el botón **INICIAR** para visualizar la ejecución del algoritmo paso a paso. La interfaz muestra el costo acumulado en cada celda visitada.

## Detener el Servidor

Presionar `Ctrl + C` en la terminal donde se está ejecutando `app.py`.
