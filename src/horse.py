from datetime import datetime


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


movements = 0
comparisons = 0
time = datetime.now()


def is_valid_position(coord, board, size):
    global comparisons

    comparisons += 1
    if 0 <= coord.x < size and 0 <= coord.y < size and board[coord.x][coord.y] == -1:
        return True

    return False


def horse_walk(current, pos, board, moves, size):
    global comparisons, movements, time

    # Limitador de 30 minutos
    comparisons += 1
    if (str(f"{datetime.now() - time}").split(':')[1] == '30'):
        return False

    comparisons += 1
    if pos == size ** 2:
        return pos != 1

    for i in range(len(moves)):
        new_coord = Coord((current.x + moves[i].x), (current.y + moves[i].y))

        comparisons += 1
        if is_valid_position(new_coord, board, size):
            movements += 1
            board[new_coord.x][new_coord.y] = pos

            comparisons += 1
            if horse_walk(new_coord, (pos + 1), board, moves, size):
                return True

            movements += 1
            board[new_coord.x][new_coord.y] = -1

    return False


if __name__ == '__main__':
    for i in range(1, 9, 1):
        size = i
        movements = 0
        comparisons = 0
        board = [[-1 for i in range(size)]for i in range(size)]
        moves = [
            Coord(2, 1), Coord(1, 2),
            Coord(-1, 2), Coord(-2, 1),
            Coord(-2, -1), Coord(-1, -2),
            Coord(1, -2), Coord(2, -1),
        ]

        initial = Coord(0, 0)
        board[initial.x][initial.y] = 0

        time = datetime.now()
        hasResulted = horse_walk(initial, 1, board, moves, size)
        time = datetime.now() - time

        print(f'\nResultado ({size}) ------------------------')
        print(f'Tempo: {time}')
        print(f'Comparações: {comparisons}')
        print(f'Movimentações: {movements}\n')
        if hasResulted:
            for i in range(size):
                for j in range(size):
                    print(board[i][j], end=' ')
                print()
        else:
            print("Not have solution")
