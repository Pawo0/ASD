from egz1btesty import runtests


def planets(D, C, T, E):
    n = len(D)
    f = [[float('inf') for _ in range(E + 1)] for _ in range(n)]
    for i in range(E + 1):
        f[0][i] = i * C[0]

    f[T[0][0]][0] = T[0][1]
    for i in range(1, n):
        for b in range(E + 1):
            if b + (D[i] - D[i - 1]) < E + 1:
                f[i][b] = min(f[i - 1][b + (D[i] - D[i - 1])], f[i][b])

            if b > 0:
                f[i][b] = min(f[i][b], f[i][b - 1] + C[i])

        if T[i][0] != i:
            f[T[i][0]][0] = min(f[T[i][0]][0], f[i][0] + T[i][1])
    return min(f[-1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=True)
