import random
from datetime import datetime

array_compare = []
array_moves = []


def calculate(num, id):
    global array_compare, array_moves

    movements = 0
    comparisons = 0
    time = datetime.now()

    n = len(num)
    best = [0] * n
    next = [None] * n
    for i in range(n - 1, -1, -1):
        movements += 1
        best[i] = 1
        for j in range(i + 1, n):
            comparisons += 1
            if num[j] > num[i] and 1 + best[j] > best[i]:
                movements += 2
                best[i] = 1 + best[j]
                next[i] = j + 1

    print(f'\nResultado ({id}) ------------------')
    print(f'Tempo: {datetime.now() - time}')
    print(f'Comparações: {comparisons}')
    print(f'Movimentações: {movements}')
    print(f'Num: {num}')
    print(f'Best: {best}')
    print(f'Next: {next}')

    array_compare.append(comparisons)
    array_moves.append(movements)


if __name__ == '__main__':
    array_x = []
    for i in range(100):
        array_x.append(i + 1)
        index = i + 1
        array = [random.randint(index, 1000) for i in range(index)]
        calculate(array, index)

    print(f'\n\n-----------------------------------')
    print(f'array_x = {array_x}')
    print(f'array_compare = {array_compare}')
    print(f'array_moves = {array_moves}')
