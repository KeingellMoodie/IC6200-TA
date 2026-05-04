from csp import (
    initialize,
    backtracking_with_inference,
    select_mrv_degree,
    _select_first,
    select_mrv,
    select_degree,
)

# Variables: nombres de los cursos
variables = ["Math", "Science", "History", "Art", "Spanish"]

# Dominio: días disponibles
domain = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Restricciones: pares de cursos que no pueden ir el mismo día
constraints = [
    "Math!=Science",
    "Math!=History",
    "Science!=Art",
    "History!=Spanish",
    "Art!=Spanish",
]

def main():
    courses = initialize(variables, domain)
    unassigned = courses[:]
    assigned = []

    if backtracking_with_inference(unassigned, assigned, constraints, select=select_mrv_degree):
        print("\nSolución encontrada:")
        for course in courses:
            print(f"  {course}")
    else:
        print("No se encontró solución.")

main()
