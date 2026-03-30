VACIO  = 0
PARED  = 1
INICIO = 2
FIN    = 3

direcciones = [(-1,0), (1,0), (0,-1), (0,1)]

class Node:
    def __init__(self, pos, parent=None):
        self.pos    = pos
        self.parent = parent

def encontrar_inicio_fin(matriz):
    inicio = fin = None
    for r in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[r][c] == INICIO:
                inicio = (r, c)
            elif matriz[r][c] == FIN:
                fin = (r, c)
    return inicio, fin

def obtener_vecinos(matriz, fila, col):
    vecinos = []
    for df, dc in direcciones:
        nf = fila + df
        nc = col  + dc
        if 0 <= nf < len(matriz) and 0 <= nc < len(matriz[0]):
            if matriz[nf][nc] != PARED:
                vecinos.append((nf, nc))
    return vecinos

def dfs(matriz):
    inicio, fin = encontrar_inicio_fin(matriz)
    if not inicio or not fin:
        return None, [{"type": "no_path"}]

    pila      = [Node(inicio)]
    visitados = set()
    pasos     = []

    while pila:
        nodo_actual = pila.pop()
        pos_actual  = nodo_actual.pos

        if pos_actual in visitados:
            continue

        visitados.add(pos_actual)
        pasos.append({"type": "visit", "pos": list(pos_actual)})

        if pos_actual == fin:
            # Reconstruir camino
            camino = []
            nodo   = nodo_actual
            while nodo:
                camino.append(list(nodo.pos))
                nodo = nodo.parent
            camino.reverse()
            pasos.append({"type": "path", "camino": camino, "costo": len(camino) - 1})
            return camino, pasos

        for nf, nc in obtener_vecinos(matriz, pos_actual[0], pos_actual[1]):
            vecino = (nf, nc)
            if vecino not in visitados:
                pila.append(Node(vecino, parent=nodo_actual))

    pasos.append({"type": "no_path"})
    return None, pasos
