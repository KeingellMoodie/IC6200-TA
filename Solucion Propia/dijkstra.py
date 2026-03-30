import heapq

VACIO  = 0
PARED  = 1
INICIO = 2
FIN    = 3

direcciones = [(-1,0), (1,0), (0,-1), (0,1)]

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
                vecinos.append((nf, nc, 1))  # costo siempre 1 en matriz
    return vecinos

def dijkstra(matriz):
    inicio, fin = encontrar_inicio_fin(matriz)
    if not inicio or not fin:
        return None, [{"type": "no_path"}]

    # (costo, posicion, camino)
    heap      = [(0, inicio, [inicio])]
    visitados = set()
    pasos     = []

    while heap:
        costo, ciudad, camino = heapq.heappop(heap)

        if ciudad in visitados:
            continue

        visitados.add(ciudad)
        pasos.append({"type": "visit", "pos": list(ciudad), "costo": costo})

        if ciudad == fin:
            camino_lista = [list(p) for p in camino]
            pasos.append({"type": "path", "camino": camino_lista, "costo": costo})
            return camino, pasos

        for nf, nc, peso in obtener_vecinos(matriz, ciudad[0], ciudad[1]):
            vecino = (nf, nc)
            if vecino not in visitados:
                heapq.heappush(heap, (costo + peso, vecino, camino + [vecino]))

    pasos.append({"type": "no_path"})
    return None, pasos
