from zad2testy import runtests


def complete_tree_string(values):
    if values:
        just = 0
        data = []

        limit = 1
        values_row = []
        branches_row = []
        prev_nodes = 0

        for i in range(1, len(values) + 1):
            curr_nodes = i - prev_nodes
            val_str = str(values[i-1])
            just = max(just, len(val_str))
            values_row.append(val_str)
            right_child_idx = 2 * i
            left_child_idx = right_child_idx - 1
            if left_child_idx < len(values):
                branches_row.append('/')
            if right_child_idx < len(values):
                branches_row.append('\\')

            if curr_nodes == limit:
                prev_nodes = i
                limit *= 2
                data.append([values_row, branches_row])
                values_row = []
                branches_row = []

        if values_row:
            data.append([values_row, branches_row])

        begin_sep = sep = 3 if just % 2 else 2
        data_iter = iter(data[::-1])
        result = [''] * (len(data) * 2 - 1)
        result[-1] = (' ' * sep).join(val.center(just) for val in next(data_iter)[0])

        # Format the tree string
        for i, (values, branches) in enumerate(data_iter):
            mul = 2 * i + 1
            # Values
            indent = (2 ** (i + 1) - 1) * (just + begin_sep) // 2
            sep = 2 * sep + just
            result[-(mul + 2)] = f"{' ' * indent}{(' ' * sep).join(val.center(just) for val in values)}"
            # Branches
            branch_indent = (3 * indent + just) // 4
            branches_row = []
            d_indent = indent - branch_indent
            branches_sep = ' ' * (2 * (d_indent - 1) + just)
            for i in range(0, len(branches), 2):
                branches_row.append(f"{branches[i]}{branches_sep}{branches[i + 1] if i + 1 < len(branches) else ''}")
            result[-(mul + 1)] = f"{' ' * branch_indent}{(' ' * (sep - 2 * d_indent)).join(branches_row)}"

        return '\n'.join(result)
    else:
        return ''

class MaxHeap:
    def __str__(self):
        # return complete_tree_string(self.tab[:self.size])
        res = ""
        for i, el in enumerate(self.tab[:self.size]):
            res += f"{i}: {el}, "
        return res[:-2]

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
        if l < n and self.tab[l][0] > self.tab[max_ind][0]:
            max_ind = l
        if r < n and self.tab[r][0] > self.tab[max_ind][0]:
            max_ind = r
        if max_ind != i:
            self.tab[max_ind], self.tab[i] = self.tab[i], self.tab[max_ind]
            self.heapify(n, max_ind)

    def build_heap(self, n):
        for i in range(self.parent(n - 1), -1, -1):
            self.heapify(n, i)

    def add(self, x):
        self.tab.insert(0,x)
        self.size += 1
        self.heapify(self.size,0)

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
        if l < n and self.tab[l][0] < self.tab[max_ind][0]:
            max_ind = l
        if r < n and self.tab[r][0] < self.tab[max_ind][0]:
            max_ind = r
        if max_ind != i:
            self.tab[max_ind], self.tab[i] = self.tab[i], self.tab[max_ind]
            self.heapify(n, max_ind)


def partition(T, p, r):
    x = T[r][0]
    i = p
    for j in range(p, r):
        if T[j][0] >= x:
            T[i], T[j] = T[j], T[i]
            i += 1
    T[r], T[i] = T[i], T[r]
    return i


def quickSort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        quickSort(T, p, q - 1)
        p = q + 1


def ksum(T: list, k, p):
    smaller = MaxHeap(len(T))
    bigger = MinHeap(len(T))
    tab = [None] * (p)
    for i in range(p):
        tab[i] = (T[i],i)
    quickSort(tab,0,p-1)
    big = tab[:k-1]
    small = tab[k:]
    bigger.add_tab(big)
    smaller.add_tab(small)

    middle = tab[k-1]
    suma = middle[0]
    for i in range(p,len(T)):
        # add new
        if T[i] > middle[0]:
            bigger.add((T[i],i))
            smaller.add(middle)
            middle = bigger.pop()
            while middle[1] < (i-p):
                middle = bigger.pop()
        elif T[i] < middle[0]:
            smaller.add((T[i],i))
        elif T[i] == middle[0]:
            smaller.add((T[i],i))
        # del old
        if T[i-p] > middle[0]:
            bigger.add(middle)
            middle = smaller.pop()
            while middle[1] <= (i-p):
                middle = smaller.pop()
        elif T[i-p] < middle[0]:
            pass
        elif T[i-p] == middle[0] and (i-p) == middle[1]:
            middle = smaller.pop()
            while middle[1] <= (i-p):
                middle = smaller.pop()
        elif T[i-p] == middle[0]:
            pass


        suma += middle[0]
    return suma

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=False)
