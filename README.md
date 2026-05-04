# Algoritmos de Búsqueda 

**Instituto Tecnológico de Costa Rica**
Escuela de Ingeniería en Computación
Curso: Inteligencia Artificial — Semestre I, 2026

**Estudiante:** Keingell Moodie J

---

## Descripción

Este repositorio contiene la implementación de los algoritmos vistos en clase. Cada algoritmo cuenta con su propia carpeta, y un README individual con instrucciones de instalación y ejecución. La mayoría incluye una interfaz visual construida con Flask y Python.

---

## Estructura del Repositorio

```
/
├── A_Star/                  ← Búsqueda heurística con distancia Manhattan
├── BFS/                     ← Búsqueda por anchura
├── DFS/                     ← Búsqueda por profundidad
├── Dijkstra/                ← Caminos mínimos en grafo ponderado
├── Minimax/                 ← Toma de decisiones en juegos de dos jugadores (Gato en este caso)
├── Hill Climbing/           ← Algoritmo Hill Climbing con optimizacion (Simulated Annealing)
└── CSP/                     ← Satisfacción de restricciones con backtracking e inferencia
```

Carpetas con interfaz visual (Flask):

```
Algoritmo/
├── app.py              ← Servidor Flask
├── algoritmo.py        ← Implementación del algoritmo
├── utils.py            ← Funciones auxiliares (donde aplica)
├── README.md           ← Instrucciones específicas del algoritmo
└── templates/
    └── index.html      ← Interfaz visual
```

Carpetas solo consola (sin Flask):

```
CSP/
├── csp.py              ← Implementación completa
├── __init__.py         ← Exportaciones del módulo
├── main.py             ← Punto de entrada
└── README.md           ← Instrucciones específicas
```

---

## Requisitos Generales

- Python 3.x — [https://www.python.org](https://www.python.org)
- Flask (para los algoritmos con interfaz visual):

```bash
pip install flask
```

El módulo CSP no requiere librerías externas.

---

## Ejecución 

### Algoritmos con interfaz visual

1. Ingresar a la carpeta del algoritmo deseado.
2. Ejecutar el servidor:

```bash
python app.py
```

3. Abrir en el navegador:

```
http://127.0.0.1:5000
```

### CSP (consola)

```bash
cd CSP
python main.py
```

Cada algoritmo tiene su propio README con instrucciones detalladas.

---

## Algoritmos Incluidos

| Algoritmo | Tipo | Óptimo | Interfaz |
|-----------|------|--------|----------|
| A* | Búsqueda informada | Sí | Visual (Flask) |
| BFS | Búsqueda no informada | Sí (pasos) | Visual (Flask) |
| DFS | Búsqueda no informada | No | Visual (Flask) |
| Dijkstra | Búsqueda no informada | Sí (costo) | Visual (Flask) |
| Minimax | Adversarial | Sí | Visual (Flask) |
| Hill Climbing | Búsqueda local | No (aproximado) | Visual (Flask) |
| CSP + AC-3 | Satisfacción de restricciones | Sí | Consola |
