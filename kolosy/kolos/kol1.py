# Paweł Czajczyk
# Program przechodzi pętlą przez wszystkie elementy i dla każdego sprawdza wszystkie wczesniejsze od niego
# czy są mniejsze. Jeśli są zwieksza licznik. Zapisuje najwiekszy wynierajac max z aktualnego i
# wczesniejszego najwiekszego i na końcku go zwraca
# Złożoność czasowa O(n^2), pamięciowa O(1)


from kol1testy import runtests


def partition(T, l, r):
    x = T[r][0]
    i = l - 1
    for j in range(l, r):
        if T[j][0] >= x:
            i += 1
            T[j], T[i] = T[i], T[j]
    T[r], T[i + 1] = T[i + 1], T[r]
    return i + 1


def quickSort(T, p, r):
    while p <= r:
        q = partition(T, p, r)
        quickSort(T, p, q - 1)
        p = q + 1


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
    for i in range(len(tab) - 1, -1, -1):
        res[tab3[tab[i][coord]] - 1] = tab[i]
        tab3[tab[i][coord]] -= 1
    for i in range(n):
        tab[i] = res[i]


# def maxrank(T):
#     n = len(T)
#     maks = 0
#     for i in range(n):
#         cnt = 0
#         for j in range(0, i):
#             if T[j] < T[i]:
#                 cnt += 1
#         maks = max(cnt, maks)
#     return maks

def maxrank(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], i)
    maks_cords = []
    counting_sort_by(T, 1)
    counting_sort_by(T, 0)
    maks_cords.append(T[-1])
    for i in range(len(T) - 2, -1, -1):
        if T[i][1] >= maks_cords[-1][1]:
            maks_cords.append(T[i])

    res = 0

    for cord in maks_cords:
        cnt = 0
        for el in T:
            if el[0] < cord[0] and el[1] < cord[1]:
                cnt += 1
        res = max(cnt, res)
    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxrank, all_tests=True)
