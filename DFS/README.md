# Algoritmo DFS 

## Descripción del Algoritmo

La Búsqueda por Profundidad (DFS, por sus siglas en inglés: *Depth-First Search*) es un algoritmo de búsqueda no informada que explora un grafo o estructura de datos siguiendo un camino hasta su nodo más profundo antes de retroceder y explorar otras ramas. Utiliza una **pila (LIFO)** como estructura principal, lo que le permite profundizar en una dirección antes de considerar alternativas.

En esta implementación, DFS opera sobre una **matriz bidimensional** y expande la búsqueda en cuatro direcciones posibles: arriba, abajo, izquierda y derecha. El algoritmo marca cada celda visitada para evitar ciclos infinitos.

Características principales:

- **Completo:** en espacios finitos, siempre encuentra una solución si existe.
- **No óptimo:** el camino encontrado no necesariamente tiene el menor número de pasos, ya que DFS no garantiza explorar los nodos más cercanos primero.

Para reconstruir el camino desde el inicio hasta el destino, se utiliza una clase `Node` que almacena la posición actual y una referencia al nodo padre, permitiendo trazar el recorrido hacia atrás al encontrar el destino.

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
DFS/
├── app.py              ← Servidor Flask y lógica principal
├── dfs.py              ← Implementación del algoritmo DFS
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

4. Presionar el botón **INICIAR** para visualizar la ejecución del algoritmo paso a paso.

## Detener el Servidor

Presionar `Ctrl + C` en la terminal donde se está ejecutando `app.py`.
