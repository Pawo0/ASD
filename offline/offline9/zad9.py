from zad9testy import runtests


def trip(M):
    n = len(M)
    m = len(M[0])
    f = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if f[i][j] == -1:
                dfs(M, f, i, j)
    # res = 0
    # for row in f:
    #     m = max(row)
    #     res = max(m,res)
    # return res
    return max(max(f[i]) for i in range(n))


def is_ok(M, f, x, y, d1, d2):
    if 0 <= x + d1 < len(M) and 0 <= y + d2 < len(M[0]) and M[x][y] < M[x + d1][y + d2] and f[x + d1][y + d2] == -1:
        return True
    return False


def is_ok_2(M, x, y):
    if 0 <= x < len(M) and 0 <= y < len(M[0]):
        return True
    return False


def dfs(M, f, x, y):
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    f[x][y] = 0
    for d1, d2 in d:
        if is_ok(M, f, x, y, d1, d2):
            dfs(M, f, x + d1, y + d2)
    m = 0
    for d1, d2 in d:
        if is_ok_2(M, x + d1, y + d2):
            m = max(m, f[x + d1][y + d2])
    f[x][y] = m + 1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(trip, all_tests=True)
