import copy

OBJECT_EMPTY = None
OBJECT_HOUSE = "🏠"
OBJECT_HOSPITAL = "🏥"


MOVE_UP = (0, -1)
MOVE_DOWN = (0, 1)
MOVE_LEFT = (-1, 0)
MOVE_RIGHT = (1, 0)


def is_free_to_move(map, move):
    x, y = move
    for i, row in enumerate(map):
        for j, element in enumerate(row):
            if x == j and y == i:
                if element is None:
                    return True
                else:
                    return False


def is_valid_move(map, move):
    x, y = move
    for i, row in enumerate(map):
        for j, element in enumerate(row):
            if x == j and y == i:
                return True
    return False


def find_objects(map, target_object_symbol):
    Simbolos = []
    for i, row in enumerate(map):
        for j, element in enumerate(row):
            if element == target_object_symbol:
                tupla = (j, i)
                Simbolos.append(tupla)
    return Simbolos


def result(map, hospital_coordinates, target_move):
    New_Map = copy.deepcopy(map)
    return result_aux(New_Map, hospital_coordinates, target_move, 1)

def result_aux(map, hospital_coordinates, target_move, stage):
    x, y = hospital_coordinates
    x1, y1 = target_move
    if stage == 1:
        for i, row in enumerate(map):
            for j, element in enumerate(row):
                if x1 == j and y1 == i:
                    map[i][j] = OBJECT_HOSPITAL
                    return result_aux(map, hospital_coordinates, target_move, 2)
    if stage == 2:
        for i, row in enumerate(map):
            for j, element in enumerate(row):
                if x == j and y == i:
                    map[i][j] = None
                    return result_aux(map, hospital_coordinates, target_move, 3)
    return map


def manhattan(pos, pos_2):
    return abs(pos[0] - pos_2[0]) + abs(pos[1] - pos_2[1])


def cost(map):
    casas = find_objects(map, OBJECT_HOUSE)
    hospitales = find_objects(map, OBJECT_HOSPITAL)
    Total = 0
    for hospital in hospitales:
        for casa in casas:
            manhattan_result = manhattan(hospital, casa)
            Total += manhattan_result
    return Total


def move(pos, pos_2):
    x, y = pos
    x1, y1 = pos_2
    return (x + x1, y + y1)


def actions(map, hospital_position):
    Moves = []
    movement = move(hospital_position, MOVE_UP)
    if is_free_to_move(map, movement) and is_valid_move(map, movement):
        Moves.append(movement)

    movement = move(hospital_position, MOVE_DOWN)
    if is_free_to_move(map, movement) and is_valid_move(map, movement):
        Moves.append(movement)

    movement = move(hospital_position, MOVE_LEFT)
    if is_free_to_move(map, movement) and is_valid_move(map, movement):
        Moves.append(movement)

    movement = move(hospital_position, MOVE_RIGHT)
    if is_free_to_move(map, movement) and is_valid_move(map, movement):
        Moves.append(movement)

    return Moves
