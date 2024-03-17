from zad2testy import runtests


class MaxHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.tab = [None] * max_size
        self.size = 0

        self.left = lambda n: 2 * n + 1
        self.right = lambda n: 2 * n + 2
        self.parent = lambda n: 0 if n < 1 else (n - 1) // 2

    def heapify(self, n, i):
        max_ind = i
        l = self.left(i)
        r = self.right(i)
        if l < n and self.tab[l] > self.tab[max_ind]:
            max_ind = l
        if r < n and self.tab[r] > self.tab[max_ind]:
            max_ind = r
        if max_ind != i:
            self.tab[max_ind], self.tab[i] = self.tab[i], self.tab[max_ind]
            self.heapify(n, max_ind)

    def build_heap(self, n):
        for i in range(self.parent(n - 1), -1, -1):
            self.heapify(n, i)

    def add(self, x):
        self.tab[self.size] = x

        self.size += 1
        self.build_heap(self.size)

    def add_tab(self, tab):
        start = self.size
        for i in range(len(tab)):
            self.tab[i + start] = tab[i]
            self.size += 1
        self.build_heap(self.size)

    def pop(self) -> int:
        to_del = self.tab[0]
        self.size -= 1
        self.tab[0] = self.tab[self.size]
        self.heapify(self.size, 0)
        self.tab[self.size] = None
        return to_del


class MinHeap(MaxHeap):
    def heapify(self, n, i):
        max_ind = i
        l = self.left(i)
        r = self.right(i)
        if l < n and self.tab[l] < self.tab[max_ind]:
            max_ind = l
        if r < n and self.tab[r] < self.tab[max_ind]:
            max_ind = r
        if max_ind != i:
            self.tab[max_ind], self.tab[i] = self.tab[i], self.tab[max_ind]
            self.heapify(n, max_ind)


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
    smaller = MaxHeap(len(T))
    bigger = MinHeap(len(T))
    tab = T[:p]
    quickSort(tab,0,p-1)
    big = tab[:k-1]
    small = tab[k:]
    bigger.add_tab(big)
    smaller.add_tab(small)

    middle = tab[k-1]
    suma = middle
    for i in range(p,len(T)):
        # add new
        if T[i] > middle:
            bigger.add(T[i])
            smaller.add(middle)
            middle = bigger.pop()
        elif T[i] < middle:
            smaller.add(T[i])

        # del old
        if T[i-p] > middle:
            bigger.add(middle)
            middle = smaller.pop()
        elif T[i-p] < middle:
            pass


        suma += middle

    return suma

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=False)
