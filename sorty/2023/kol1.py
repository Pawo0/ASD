from kol1testy import runtests


def partition(T, l, r):
    x = T[r]
    i = l - 1
    for j in range(l, r):
        if T[j] >= x:
            i += 1
            T[j], T[i] = T[i], T[j]
    T[r], T[i + 1] = T[i + 1], T[r]
    return i + 1


def quick_select(tab, l, r, x):
    if l <= r:
        q = partition(tab, l, r)
        if x == q:
            return q
        elif q > x:
            return quick_select(tab, l, q - 1,x)
        else:
            return quick_select(tab, q + 1, r,x)


def ksum(T, k, p):
    res = 0
    for i in range(p,len(T)+1):
        tab = T[i-p:i]
        x = quick_select(tab,0,p-1,k-1)
        res += tab[x]

    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=True)
