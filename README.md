# Algoritmos de Búsqueda 

**Instituto Tecnológico de Costa Rica**
Escuela de Ingeniería en Computación
Curso: Inteligencia Artificial — Semestre I, 2026

**Estudiante:** Keingell Moodie J

---

## Descripción

Este repositorio contiene la implementación de los cinco algoritmos vistos en clase. Cada algoritmo cuenta con su propia carpeta, interfaz visual interactiva construida con Flask y Python, y un README individual con instrucciones de instalación y ejecución.

---

## Estructura del Repositorio

```
/
├── A_Star/         ← Búsqueda heurística con distancia Manhattan
├── BFS/            ← Búsqueda por amplitud
├── DFS/            ← Búsqueda por profundidad
├── Dijkstra/       ← Caminos mínimos en grafo ponderado
└── Minimax/        ← Toma de decisiones en juegos de dos jugadores
```

Cada carpeta contiene:

```
Algoritmo/
├── app.py              ← Servidor Flask
├── algoritmo.py        ← Implementación del algoritmo
├── utils.py            ← Funciones auxiliares (donde aplica)
├── README.md           ← Instrucciones específicas del algoritmo
└── templates/
    └── index.html      ← Interfaz visual
```

---

## Requisitos Generales

- Python 3.x — [https://www.python.org](https://www.python.org)
- Flask

```bash
pip install flask
```

---

## Ejecución Rápida

1. Ingresar a la carpeta del algoritmo deseado.
2. Ejecutar el servidor:

```bash
python app.py
```

3. Abrir en el navegador:

```
http://127.0.0.1:5000
```

Cada algoritmo tiene su propio README con instrucciones detalladas.

---

## Algoritmos Incluidos

| Algoritmo | Tipo | Óptimo | Estructura |
|-----------|------|--------|------------|
| A* | Búsqueda informada | Sí | Cola de prioridad + heurística Manhattan |
| BFS | Búsqueda no informada | Sí (pasos) | Cola FIFO |
| DFS | Búsqueda no informada | No | Pila LIFO |
| Dijkstra | Búsqueda no informada | Sí (costo) | Cola de prioridad |
| Minimax | Adversarial | Sí | Árbol de juego recursivo |
