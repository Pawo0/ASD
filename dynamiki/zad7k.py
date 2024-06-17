from zad7ktesty import runtests


def ogrodnik(T, D, Z, l):
    vis = [[False for _ in range(len(T[0]))] for _ in range(len(T))]
    C = []
    for i in range(len(D)):
        C.append(depth(T, 0, D[i], 0, vis))
    n = len(D)
    f = [[0 for _ in range(l + 1)] for _ in range(n)]
    for b in range(C[0], l + 1):
        f[0][b] = Z[0]
    for b in range(l + 1):
        for i in range(1, n):
            f[i][b] = f[i - 1][b]
            if b - C[i] >= 0:
                f[i][b] = max(f[i][b], f[i - 1][b - C[i]] + Z[i])
    return f[-1][-1]


def is_ok(T, x, y, vis):
    if 0 <= x < len(T) and 0 <= y < len(T[0]) and T[x][y] and not vis[x][y]:
        return True
    return False


def depth(T, x, y, res, vis):
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = [(x, y)]
    while q:
        x, y = q.pop()
        vis[x][y] = True
        res += T[x][y]
        for d1, d2 in d:
            if is_ok(T, x + d1, y + d2, vis):
                q.append((x + d1, y + d2))
                vis[x + d1][y + d2] = True
    return res


runtests(ogrodnik, all_tests=True)
