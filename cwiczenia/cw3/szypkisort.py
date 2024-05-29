def partition(T, p, r) -> int:
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quick_sort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        if q > (p + r) // 2:
            quick_sort(T, p, r)
            r = q - 1
        else:
            quick_sort(T, p, q - 1)
            p = q + 1


def q_sort(T, p, r):
    s = []
    s.append((p, r))
    while len(s) != 0:
        p, r = s.pop()
        q = partition(T, p, r)
        if p < q - 1:
            s.append((p, q - 1))
        if q + 1 < r:
            s.append((q + 1, r))
