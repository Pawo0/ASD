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
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] >= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[r], T[i + 1] = T[i + 1], T[r]
    return i + 1


def quickSort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        quickSort(T, p, q - 1)
        p = q + 1


def ksum(T: list, k, p):
    tab = T[:p]
    idx = tab.copy()
    quickSort(tab, 0, len(tab) - 1)
    suma = tab[k - 1]
    # res = f"{tab[k - 1]}"
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
        # res += f" + {tab[k - 1]}"
    # print(res)
    return suma


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=True)
