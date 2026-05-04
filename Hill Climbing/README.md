# Simulated Annealing — Optimización de Hospitales

## Descripción del Algoritmo

Simulated Annealinges un algoritmo de búsqueda local inspirado en un proceso donde un material se calienta y luego se enfría lentamente para reducir defectos en su estructura. En IA, esta técnica se utiliza para encontrar soluciones óptimas o lo mas cercanas posibles a un caso optimo, en problemas de optimización.

A diferencia del algoritmo Hill Climbing, que siempre acepta únicamente movimientos que mejoran la solución, Simulated Annealing puede **aceptar ocasionalmente movimientos que empeoran el estado actual**, en base a una probabilidad controlada por un parámetro llamado **temperatura**. Esto le permite escapar de óptimos locales y explorar un espacio de búsqueda más amplio.

En este caso, el algoritmo optimiza las posiciones de hospitales en una matriz para **minimizar la suma de distancias Manhattan** entre cada hospital y todas las casas del mapa.

### Parámetros del algoritmo

| Parámetro | Descripción | Valor usado |
|-----------|-------------|-------------|
| `T_initial` | Temperatura inicial (exploración alta) | `1000` |
| `T_min` | Temperatura mínima (criterio de parada) | `0.1` |
| `cooling_rate` | Factor de enfriamiento por iteración | `0.995` |

### Función de aceptación

En cada iteración, si el movimiento candidato **no mejora** el costo actual, se acepta con probabilidad:

```
P = e^(-(costo_candidato - costo_actual) / temperatura)
```

Cuando la temperatura es mayor, mayor es la probabilidad de aceptar movimientos malos. A medida que la temperatura disminuye, el algoritmo se vuelve más selectivo, comportándose cada vez mas cerca a un Hill Climbing convencional.

### Representación del mapa

| Símbolo | Significado |
|---------|-------------|
| `🏠` | Casa |
| `🏥` | Hospital |
| `None` | Celda vacía |

---

## Requisitos de Instalación

### 1. Python

Verificar que Python esté instalado:

```bash
python --version
```

Si no está instalado, descargarlo desde [https://www.python.org](https://www.python.org).

### 2. Flask

```bash
pip install flask
```

---

## Estructura de Archivos

```
Simulated_Annealing/
├── app.py                  ← Servidor Flask, ejecuta el algoritmo y expone la API
├── simulated_annealing.py  ← Implementación del algoritmo
├── utils.py                ← Funciones auxiliares: cost, actions, result, find_objects
└── templates/
    └── index.html          ← Interfaz visual 

> **Importante:** La carpeta `templates` debe estar en el mismo directorio que `app.py`.

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

4. Presionar **INICIAR**.

## Detener el Servidor

Presionar `Ctrl + C` en la terminal donde se está ejecutando `app.py`.
