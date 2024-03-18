from zad2testy import runtests


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


def bin_search(tab, i, x, y):
    mid = (x + y) // 2
    if tab[mid] == i:
        return mid
    elif tab[mid] < i:
        return bin_search(tab, i, x, mid - 1)
    else:
        return bin_search(tab, i, mid + 1, y)


def bin_search_lower(tab, x):
    l = 0
    r = len(tab) - 1
    while l <= r:
        mid = (l + r) // 2
        if tab[mid] < x:
            r = mid - 1
        else:
            l = mid + 1
    return l


def ksum(T: list, k, p):
    tab = T[:p]
    quickSort(tab, 0, len(tab) - 1)
    suma = tab[k - 1]
    for i in range(p, len(T)):
        id_to_del = i - p
        id_to_add = i
        to_del = bin_search(tab, T[id_to_del], 0, len(tab))
        tab.pop(to_del)
        to_add = bin_search_lower(tab, T[id_to_add])
        tab.insert(to_add, T[id_to_add])

        suma += tab[k - 1]
    return suma


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=True)
