from zad7testy import runtests


def maze(L):
    n = len(L)
    # 0 up, 1 left, 2 down
    f = [[[-1 for direct in range(3)] for _ in range(n)] for _ in range(n)]
    for i in range(3):
        f[0][0][i] = 0
    for y in range(n):
        for x in range(n):
            if x == 0 and y == 0:
                continue
            if L[x][y] != '#':
                # left
                if y - 1 >= 0:
                    m = max(f[x][y - 1][0], f[x][y - 1][1], f[x][y - 1][2])
                    if m != -1:
                        f[x][y][1] = m + 1
                # up
                if x - 1 >= 0:
                    m = max(f[x - 1][y][2], f[x - 1][y][1])
                    if m != -1:
                        f[x][y][2] = m + 1

        for x in range(n - 1, -1, -1):
            if L[x][y] != '#':
                # down
                if x + 1 < n:
                    m = max(f[x + 1][y][1], f[x + 1][y][0])
                    if m != -1:
                        f[x][y][0] = m + 1
    return max(f[n - 1][n - 1][i] for i in range(3))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)
