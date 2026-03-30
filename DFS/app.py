from flask import Flask, jsonify, render_template
from dfs      import dfs

app = Flask(__name__)

# ── Matriz compartida por todos los algoritmos ──────────────
matriz = [
    [2, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 3],
]

# ── Rutas ────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/matriz")
def get_matriz():
    return jsonify({"matriz": matriz})

@app.route("/api/resolver/dfs")
def resolver_dfs():
    _, pasos = dfs(matriz)
    return jsonify({"pasos": pasos})


if __name__ == "__main__":
    app.run(debug=True)
