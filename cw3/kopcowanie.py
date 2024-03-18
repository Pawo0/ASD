def parent(n):
    return (n - 1) // 2 if n > 0 else 0


def decrease_key(T, i, x):
    # if x > i
    p = parent(i)
    T[i] = x
    while T[p] > T[i]:
        T[p], T[i] = T[i], T[p]
        i = p
        p = parent(i)


class Heap:
    def __init__(self, max_size):
        self.T = [None] * max_size
        self.max_size = max_size
        self.size = 0


def heap_add(H: Heap, x):
    if H.size < H.max_size:
        decrease_key(H.T, H.size, x)
        H.size += 1
