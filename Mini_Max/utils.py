import copy

PLAYER_X = "X"
PLAYER_O = "O"


def is_free_to_mark(board, movement):
    x, y = movement
    return not board[x][y]


def players(board):
    if empty_matriz(board):
        return PLAYER_X
    Cant_X = 0
    Cant_O = 0
    for row in board:
        for element in row:
            if element == PLAYER_X:
                Cant_X += 1
            if element == PLAYER_O:
                Cant_O += 1
    if Cant_O > Cant_X:
        return PLAYER_X
    if Cant_O == Cant_X:
        return PLAYER_X
    else:
        return PLAYER_O


def empty_matriz(board):
    for row in board:
        for element in row:
            if element is not None:
                return False
    return True


def actions(board):
    possibly_moves = []
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            if element is None:
                possibly_moves.append((i, j))
    return possibly_moves


def result(board, action):
    new_board = copy.deepcopy(board)
    next_player = players(board)
    i, j = action
    new_board[i][j] = next_player
    return new_board


def terminal(board):
    if vertical_victory(board) == 1 or vertical_victory(board) == -1:
        return True
    if horizontal_victory(board) == 1 or horizontal_victory(board) == -1:
        return True
    if diagonal_victory(board) == 1 or diagonal_victory(board) == -1:
        return True
    if antidiagonal_victory(board) == 1 or antidiagonal_victory(board) == -1:
        return True
    else:
        return full_matriz(board)


def vertical_victory(board):
    Amount_X = 0
    Amount_O = 0
    for i in range(3):
        counter = i
        for row in board:
            if row[counter] == PLAYER_X:
                Amount_X += 1
            elif row[counter] == PLAYER_O:
                Amount_O += 1
        if Amount_O == 3 or Amount_X == 3:
            break
        else:
            Amount_X = 0
            Amount_O = 0
    if Amount_O == 3:
        return -1
    elif Amount_X == 3:
        return 1
    else:
        return 0


def horizontal_victory(board):
    Amount_X = 0
    Amount_O = 0
    for row in board:
        for element in row:
            if element == PLAYER_X:
                Amount_X += 1
            elif element == PLAYER_O:
                Amount_O += 1
        if Amount_O == 3 or Amount_X == 3:
            break
        else:
            Amount_X = 0
            Amount_O = 0
    if Amount_O == 3:
        return -1
    elif Amount_X == 3:
        return 1
    else:
        return 0


def diagonal_victory(board):
    Amount_X = 0
    Amount_O = 0
    counter = 0
    for row in board:
        if row[counter] == PLAYER_X:
            Amount_X += 1
        elif row[counter] == PLAYER_O:
            Amount_O += 1
        counter += 1
    if Amount_O == 3:
        return -1
    elif Amount_X == 3:
        return 1
    else:
        return 0


def antidiagonal_victory(board):
    Amount_X = 0
    Amount_O = 0
    counter = 2
    for row in board:
        if row[counter] == PLAYER_X:
            Amount_X += 1
        elif row[counter] == PLAYER_O:
            Amount_O += 1
        counter -= 1
    if Amount_O == 3:
        return -1
    elif Amount_X == 3:
        return 1
    else:
        return 0


def full_matriz(board):
    for row in board:
        for element in row:
            if element is None:
                return False
    return True


def utility(board):
    if vertical_victory(board) == 1 or vertical_victory(board) == -1:
        return vertical_victory(board)
    if horizontal_victory(board) == 1 or horizontal_victory(board) == -1:
        return horizontal_victory(board)
    if diagonal_victory(board) == 1 or diagonal_victory(board) == -1:
        return diagonal_victory(board)
    if antidiagonal_victory(board) == 1 or antidiagonal_victory(board) == -1:
        return antidiagonal_victory(board)
    return 0
