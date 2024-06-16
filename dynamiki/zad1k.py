from zad1ktesty import runtests


def roznica(S):
    print(S)
    n = len(S)
    # f[i][j] liczba 1 i 0 od i do j
    p = [1,-1]
    res = -1
    f = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        f[i][i] = p[int(S[i])]
        for j in range(i+1,n):
            f[i][j] = f[i][j-1] + p[int(S[j])]
            res = max(res, f[i][j])

    if res == n:
        return -1
    return res

runtests(roznica)
