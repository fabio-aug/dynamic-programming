
def calculate(num):
    n = len(num)
    best = [0] * n

    for i in range(n - 1, -1, -1):
        best[i] = 1
        for j in range(i + 1, n):
            if num[j] > num[i] and 1 + best[j] > best[i]:
                best[i] = 1 + best[j]

    print(best)
    print(max(best))


if __name__ == '__main__':
    array = [7, 6, 10, 3, 4, 1, 8, 9, 5, 2, 11, 14, 15, 46, 13, 10]
    calculate(array)

