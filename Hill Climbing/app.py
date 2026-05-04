from flask import Flask, jsonify, render_template
import utils
import copy
from simulated_annealing import simulated_annealing

app = Flask(__name__)

# ── Mapa inicial ─────────────────────────────────────────────
INITIAL_MAP = [
    [None, None, None, None, utils.OBJECT_HOSPITAL, None, None, None, utils.OBJECT_HOUSE, None],
    [None, None, utils.OBJECT_HOUSE, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, utils.OBJECT_HOUSE, None, None, None, None, None, None, None, utils.OBJECT_HOSPITAL],
    [None, None, None, None, None, None, utils.OBJECT_HOUSE, None, None, None],
]

# Parámetros del algoritmo
T_INITIAL    = 1000
T_MIN        = 0.1
COOLING_RATE = 0.995


def serialize_map(m):
    """Convierte el mapa a formato JSON-serializable."""
    result = []
    for row in m:
        result.append([cell if cell is not None else None for cell in row])
    return result


def run_with_steps(map, T_min, T_initial, cooling_rate):
    """
    Corre simulated annealing y guarda snapshots del mapa
    cada vez que hay una mejora, para animar la búsqueda.
    """
    import random, math

    current_map  = copy.deepcopy(map)
    current_cost = utils.cost(current_map)
    temperature  = T_initial
    pasos        = []

    pasos.append({
        "map":         serialize_map(current_map),
        "cost":        current_cost,
        "temperature": round(temperature, 2),
        "mensaje":     f"Estado inicial — costo: {current_cost}",
        "tipo":        "inicial"
    })

    iteracion = 0
    while temperature > T_min:
        best_map  = current_map
        best_cost = current_cost
        hospitals = utils.find_objects(current_map, utils.OBJECT_HOSPITAL)

        if not hospitals:
            temperature *= cooling_rate
            continue

        canditate_hospital = random.choice(hospitals)
        moves_list = utils.actions(current_map, canditate_hospital)

        if not moves_list:
            temperature *= cooling_rate
            continue

        candidate_move = random.choice(moves_list)
        candidate_map  = utils.result(current_map, canditate_hospital, candidate_move)
        candidate_cost = utils.cost(candidate_map)
        cost_difference = candidate_cost - current_cost

        tipo = "sin_cambio"
        if candidate_cost < best_cost:
            best_map  = candidate_map
            best_cost = candidate_cost
            tipo      = "mejora"
        else:
            random_num = random.random()
            acceptance = math.exp(-cost_difference / temperature)
            if random_num < acceptance:
                best_map  = candidate_map
                best_cost = candidate_cost
                tipo      = "aceptado"

        temperature  *= cooling_rate
        current_map   = best_map
        current_cost  = best_cost
        iteracion    += 1

        # Solo guardar pasos relevantes para la animación
        if tipo in ("mejora", "aceptado") or iteracion % 300 == 0:
            pasos.append({
                "map":         serialize_map(current_map),
                "cost":        current_cost,
                "temperature": round(temperature, 4),
                "mensaje":     f"It. {iteracion} — T={round(temperature,2)} — costo: {current_cost} ({tipo})",
                "tipo":        tipo
            })

    pasos.append({
        "map":         serialize_map(current_map),
        "cost":        current_cost,
        "temperature": round(temperature, 4),
        "mensaje":     f"Resultado final — costo óptimo: {current_cost}",
        "tipo":        "final"
    })

    return pasos


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/mapa_inicial")
def mapa_inicial():
    return jsonify({
        "map":  serialize_map(INITIAL_MAP),
        "cost": utils.cost(INITIAL_MAP),
        "rows": len(INITIAL_MAP),
        "cols": len(INITIAL_MAP[0]),
    })


@app.route("/api/resolver")
def resolver():
    pasos = run_with_steps(INITIAL_MAP, T_MIN, T_INITIAL, COOLING_RATE)
    return jsonify({"pasos": pasos})


if __name__ == "__main__":
    app.run(debug=True)
