from zad2testy import runtests


def merge(T, t1, t2):
    n1, n2 = len(t1), len(t2)
    i = j = k = 0
    while i < n1 and j < n2:
        if t1[i] >= t2[j]:
            T[k] = t1[i]
            i += 1
            k += 1
        else:
            T[k] = t2[j]
            j += 1
            k += 1
    while i < n1:
        T[k] = t1[i]
        i += 1
        k += 1
    while j < n2:
        T[k] = t2[j]
        j += 1
        k += 1


def mergeSort(T):
    if len(T) > 1:
        mid = len(T) // 2
        t1 = T[:mid]
        t2 = T[mid:]
        mergeSort(t1)
        mergeSort(t2)
        merge(T, t1, t2)


def partition(T, p, r):
    q = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] >= q:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def select(T, p, r, k):
    if p == r: return T[p]
    q = partition(T, p, r)
    if k == q:
        return T[q]
    elif k < q:
        return select(T, p, q - 1, k)
    else:
        return select(T, q + 1, r, k)


def ksum(T: list, k, p):
    tab = T[:p]
    idx = tab.copy()
    mergeSort(tab)
    suma = tab[k - 1]
    for i in range(p, len(T)):
        x = (i) % (p)
        search = idx[x]
        tab.remove(search)
        put = T[i]
        if tab[-1] >= put:
            tab.append(put)
        else:
            for j in range(len(tab)):
                if tab[j] <= put:
                    tab.insert(j, put)
                    break
        idx[x] = put
        suma += tab[k - 1]

    return suma


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=True)
