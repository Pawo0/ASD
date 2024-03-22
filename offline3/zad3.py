from zad3testy import runtests


def counting_sort_by(tab, coord):
    n = len(tab)
    res = [None] * n
    maxy = 0
    for x in tab:
        maxy = max(maxy, x[coord])
    tab3 = [0] * (maxy + 1)
    for i in range(n):
        tab3[tab[i][coord]] += 1
    for i in range(1, maxy + 1):
        tab3[i] += tab3[i - 1]
    for i in range(len(tab)-1, -1, -1):
        res[tab3[tab[i][coord]] - 1] = tab[i]
        tab3[tab[i][coord]] -= 1
    for i in range(n):
        tab[i] = res[i]


def dominance(P):
    maks_cords = []
    counting_sort_by(P, 1)
    counting_sort_by(P, 0)
    maks_cords.append(P[-1])
    for i in range(len(P)-2,-1,-1):
        if P[i][1] >= maks_cords[-1][1]:
            maks_cords.append(P[i])

    res = 0

    for cord in maks_cords:
        cnt = 0
        for el in P:
            if el[0] < cord[0] and el[1] < cord[1]:
                cnt += 1
        res = max(cnt,res)
    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(dominance, all_tests=True)
