"""
Paweł Czajczyk
algorytm na początku wybiera k pierwszych wyrazów i je sortuje mergesortem, jeśli zostaną jeszcze jakies liczby
to po kolei bierze każda i przyrównuje z k końcowymi wyrazami posortowanej juz listy
Złożoność: k*logk+(n-k)*k
"""
from zad1testy import Node, runtests


def split(p):
    if p is None: return None, None
    start = p
    while p.next is not None and p.val <= p.next.val:
        p = p.next
    rest = p.next
    p.next = None
    return start, rest


def merge(p, q):
    if p is None:
        return q
    if q is None:
        return p
    res = Node()
    start = res
    while p is not None and q is not None:
        if p.val <= q.val:
            res.next = p
            p = p.next
        else:
            res.next = q
            q = q.next
        res = res.next
        res.next = None
    if p is not None:
        res.next = p
    elif q is not None:
        res.next = q
    while res.next is not None:
        res = res.next
    return start.next, res


def mergesort(p):
    while True:
        cnt = 0
        tmp_res = Node()
        tail = tmp_res
        while p is not None:
            s1, p = split(p)
            cnt += 1
            if p is not None:
                s2, p = split(p)
                cnt += 1
                tail.next, tail = merge(s1, s2)
            else:
                tail.next = s1

        p = tmp_res.next

        if cnt <= 2:
            break
    return p


def cut_rest(p):
    rest = False
    to_put = None
    if p is not None:
        to_put = p.next
        p.next = None
        rest = True
    return rest, to_put


def sort_rest(to_put, k_start):
    while to_put.next is not None:
        tmp_to_put = to_put.next
        tmp_k_start = k_start
        put_in_last_k(k_start, to_put)

        k_start = tmp_k_start.next
        to_put = tmp_to_put

    put_in_last_k(k_start, to_put)


def put_in_last_k(k_start, to_put):
    while k_start.next is not None:
        if k_start.next.val >= to_put.val:
            to_put.next = k_start.next
            k_start.next = to_put
            break
        k_start = k_start.next
    else:
        k_start.next = to_put
        k_start.next.next = None


def SortH(p, k):
    start = Node()
    start.next = p
    for _ in range(k):
        p = p.next
    rest, to_put = cut_rest(p)
    start.next = mergesort(start.next)
    k_start = start

    # mamy juz postortowane k pierwszych
    if rest:
        sort_rest(to_put, k_start)
    return start.next


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(SortH, all_tests=True)
