# counting ---------------------------------------------------------------------
def counting_sort(tab, k):
    n = len(tab)
    res = [None] * n
    C = [0] * (k + 1)
    for i in range(n):
        C[tab[i]] += 1
    for i in range(1, k):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        res[C[tab[i]] - 1] = tab[i]
        C[tab[i]] -= 1
    for i in range(n):
        tab[i] = res[i]


# radix ---------------------------------------------------------------------
def count_sort_by(T, by):
    res = [None] * len(T)
    C = [0] * (ord('z') - ord('a') + 1)
    for item in T:
        idx = ord(item[by]) - ord('a')
        C[idx] += 1
    for i in range(1, len(C)):
        C[i] = C[i - 1] + C[i]
    for i in range(len(T) - 1, -1, -1):
        idx = ord(T[i][by]) - ord('a')
        res[C[idx] - 1] = T[i]
        C[idx] -= 1
    for i in range(len(T)):
        T[i] = res[i]


def radix_sort(T, n):
    for i in range(n - 1, -1, -1):
        count_sort_by(T, i)


# quick ---------------------------------------------------------------------

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
            return quick_select(tab, l, q - 1, x)
        else:
            return quick_select(tab, q + 1, r, x)


def quickSort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        quickSort(T, p, q - 1)
        p = q + 1


# merge ---------------------------------------------------------------------

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


# bin search ---------------------------------------------------------------------
def bin_search(tab, x, l, r):
    while l <= r:
        mid = (l + r) // 2
        if tab[mid] == x:
            return mid
        elif tab[mid] < x:
            r = mid - 1
        else:
            l = mid + 1
    return l


# insert ---------------------------------------------------------------------
def insert_sort(T):
    for i in range(0, len(T)):
        min_id = i
        for j in range(i + 1, len(T)):
            if T[j] < T[min_id]:
                min_id = j
        T[i], T[min_id] = T[min_id], T[i]



