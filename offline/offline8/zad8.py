from zad8testy import runtests


def parking(X, Y):
    n = len(X)
    m = len(Y)
    # f[i][j] do i tego domku, uzywajac działek tylko do j - włącznie albo minimalne wczesniejsze
    f = [[float('inf') for j in range(m)] for i in range(n)]

    f[0][0] = abs(X[0] - Y[0])
    j = 1
    while j < m:
        f[0][j] = min(abs(X[0] - Y[j]), f[0][j - 1])
        j += 1

    for i in range(1, n):
        j = i
        while j < m - (n - i - 1):
            f[i][j] = min(f[i - 1][j - 1] + abs(X[i] - Y[j]), f[i][j - 1])
            j += 1

    return min(f[-1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)
