from flask import Flask, jsonify, render_template
from minimax import ai_play
from utils import terminal, utility, result, players, actions

app = Flask(__name__)


def simular_partida():
    """
    Simula una partida completa con Minimax y devuelve todos los estados.
    """
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

    estados = []
    estados.append({
        "board": [row[:] for row in board],
        "jugador": None,
        "accion": None,
        "mensaje": "Tablero inicial"
    })

    while not terminal(board):
        jugador_actual = players(board)
        accion = ai_play(board)
        if accion is None:
            break
        board = result(board, accion)
        estados.append({
            "board": [row[:] for row in board],
            "jugador": jugador_actual,
            "accion": list(accion),
            "mensaje": f"{jugador_actual} juega en ({accion[0]}, {accion[1]})"
        })

    score = utility(board)
    if score == 1:
        resultado = "¡X gana!"
    elif score == -1:
        resultado = "¡O gana!"
    else:
        resultado = "Empate"

    estados.append({
        "board": [row[:] for row in board],
        "jugador": None,
        "accion": None,
        "mensaje": resultado,
        "fin": True,
        "score": score
    })

    return estados


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/simular")
def simular():
    estados = simular_partida()
    return jsonify({"estados": estados})


if __name__ == "__main__":
    app.run(debug=True)
