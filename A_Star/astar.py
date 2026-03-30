import heapq

VACIO  = 0
PARED  = 1
INICIO = 2
FIN    = 3

direcciones = [(-1,0), (1,0), (0,-1), (0,1)]

def manhattan(actual, meta):
    return abs(actual[0] - meta[0]) + abs(actual[1] - meta[1])

def obtener_vecinos(matriz, fila, col):
    vecinos = []
    for df, dc in direcciones:
        nf = fila + df
        nc = col  + dc
        if 0 <= nf < len(matriz) and 0 <= nc < len(matriz[0]):
            if matriz[nf][nc] != PARED:
                vecinos.append((nf, nc, 1))
    return vecinos

def encontrar_inicio_fin(matriz):
    inicio = fin = None
    for r in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[r][c] == INICIO:
                inicio = (r, c)
            elif matriz[r][c] == FIN:
                fin = (r, c)
    return inicio, fin

def a_star(matriz):
    inicio, fin = encontrar_inicio_fin(matriz)
    if not inicio or not fin:
        return None, [{"type": "no_path"}]

    heap      = [(0 + manhattan(inicio, fin), 0, inicio)]
    g_score   = {inicio: 0}
    came_from = {}
    visitados = set()
    pasos     = []

    while heap:
        f, g, actual = heapq.heappop(heap)

        if actual in visitados:
            continue
        visitados.add(actual)

        h = f - g
        pasos.append({"type": "visit", "pos": list(actual), "g": g, "h": h, "f": f})

        if actual == fin:
            camino = []
            nodo   = actual
            while nodo in came_from:
                camino.append(list(nodo))
                nodo = came_from[nodo]
            camino.append(list(inicio))
            camino.reverse()
            pasos.append({"type": "path", "camino": camino, "costo": g})
            return camino, pasos

        for nf, nc, costo in obtener_vecinos(matriz, actual[0], actual[1]):
            vecino = (nf, nc)
            if vecino in visitados:
                continue
            g_nuevo = g + costo
            if g_nuevo < g_score.get(vecino, float('inf')):
                g_score[vecino]   = g_nuevo
                came_from[vecino] = actual
                h = manhattan(vecino, fin)
                heapq.heappush(heap, (g_nuevo + h, g_nuevo, vecino))

    pasos.append({"type": "no_path"})
    return None, pasos
