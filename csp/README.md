# CSP — Backtracking con Inferencia 

## Descripción del Algoritmo

Los Problemas de Satisfacción de Restricciones (*Constraint Satisfaction Problems*, CSP) problemas los cuales en inteligencia artificial buscan asignar valores a un conjunto de variables de forma que se satisfagan todas las restricciones definidas entre ellas.

En esta implementación se resuelve un problema de **asignación de cursos a días de la semana**, donde las restricciones dicen qué pares de cursos **no pueden** ser asignados el mismo día.

### Algoritmos implementados

**Backtracking con Inferencia** es la estrategia principal utilizada. Combina dos técnicas:

**1. Backtracking:** algoritmo de búsqueda recursiva que asigna valores a las variables una por una. Si en algún punto una assignacion no cumple una restricción, el algoritmo retrocede y prueba otro valor.

**2. AC-3 (Arc Consistency 3):** algoritmo de inferencia que se ejecuta después de cada asignación. Lo que hace es eliminar los valores que ya no pueden ser parte de ninguna solución válida, para asi reducir el espacio de búsqueda.

### Heurísticas de selección de variable

El algoritmo permite diferentes estrategias para elegir qué variable asignar a continuación:

| Heurística | Descripción |
|------------|-------------|
| `_select_first` | Selecciona la primera variable sin asignar (sin heurística) |
| `select_mrv` | *Minimum Remaining Values* — elige la variable con el dominio más pequeño |
| `select_degree` | Elige la variable con más restricciones activas |
| `select_mrv_degree` | Combina MRV como criterio principal y grado como desempate |

### Flujo general

```
inicializar cursos con su dominio
    → seleccionar variable (heurística)
        → asignar un valor del dominio
            → verificar consistencia
                → ejecutar AC-3 para reducir dominios
                    → continuar recursivamente
                        → si falla: retroceder y restaurar dominios
```

---

## Requisitos de Instalación

### Python

Verificar que Python esté instalado:

```bash
python --version
```

Si no está instalado, descargarlo desde [https://www.python.org](https://www.python.org).


---

## Estructura de Archivos

```
CSP/
├── csp.py              ← Implementación completa: Course, backtracking, AC-3, heurísticas
├── __init__.py         ← Exportaciones del módulo
└── main.py             ← Punto de entrada: define variables, dominio, restricciones y corre el algoritmo
```

---

## Instrucciones de Ejecución

### Configurar `main.py`

El archivo `main.py` define el problema, como las variables, el dominio, las restricciones y ademas de eso, ejecuta el algoritmo. 

### Ejecutar desde la terminal

```bash
python main.py
```

---

## Cambiar la heurística de selección

En `main.py` se puede cambiar el parámetro `select` para comparar el comportamiento con otras heuristicas:

```python
from csp import select_mrv, select_degree, select_mrv_degree, _select_first

# Opciones:
backtracking_with_inference(unassigned, assigned, constraints, select=_select_first)      # sin heurística
backtracking_with_inference(unassigned, assigned, constraints, select=select_mrv)         # MRV
backtracking_with_inference(unassigned, assigned, constraints, select=select_degree)      # grado
backtracking_with_inference(unassigned, assigned, constraints, select=select_mrv_degree)  # MRV + grado
```
