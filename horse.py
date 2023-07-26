class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


size = 7
board = []
moves = [
    Coord(2, 1),    # Right Top
    Coord(2, -1),   # Right Bottom
    Coord(-2, 1),   # Left Top
    Coord(-2, -1),  # Left Bottom
    Coord(1, 2),    # Top Right
    Coord(-1, 2),   # Top Left
    Coord(1, -2),   # Bottom Right
    Coord(-1, -2)   # Bottom Left
]


def create_matrix():
    global size
    global board

    aux1 = []
    for i in range(size):
        aux2 = []
        for j in range(size):
            aux2.append(-1)
        aux1.append(aux2)

    aux1[0][0] = 0
    board = aux1


def print_matrix():
    global size
    global board

    for i in range(size):
        for j in range(size):
            print(board[i][j], end=' ')
        print()


def is_valid_position(coord):
    global size
    global board

    if 0 <= coord.x < size and 0 <= coord.y < size and board[coord.x][coord.y] == -1:
        return True

    return False


def horse_walk(current, pos):
    global size
    global board
    global moves

    if pos == size ** 2:
        return True

    for i in range(8):
        new_coord = Coord(current.x + moves[i].x, current.y + moves[i].y)

        if is_valid_position(new_coord):
            board[new_coord.x][new_coord.y] = pos

            if horse_walk(new_coord, pos + 1):
                return True

            board[new_coord.x][new_coord.y] = -1

    return False


if __name__ == '__main__':
    create_matrix()

    if horse_walk(Coord(0, 0), 1):
        print_matrix()
    else:
        print("Not have solution")
