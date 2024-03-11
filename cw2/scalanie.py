class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"val:{self.val}, next:{self.next}"


def n_series(L):
    """L - wartownik głowy listy"""
    res = Node()
    tail = res
    if L.next is None:
        return L
    val = L.next.val
    while L.next is not None and L.next.val >= val:
        tail.next = L.next
        tail = tail.next
        L.next = L.next.next
        tail.next = None
        val = tail.val
    return res, L


def merge(a,b):
    L = Node()
    tail = L
    while a.next is not None and b.next is not None:
        if a.next.val >= b.next.val:
            tail.next = b.next
            tail = tail.next
        else:
            tail.next = a.next
            tail = tail.next
        tail.next = None
    if a.next is not None:
        tail.next = a.next
    elif b.next is not None:
        tail.next = b.next

    while tail.next is not None:
        tail = tail.next
    return L, tail


def sort(L):
    while True:
        cnt = 0
        res = Node()
        tail = res
        while L.next is not None:
            s1, L = n_series(L)
            cnt += 1
            if L.next is not None:
                s2, L = n_series(L)
                cnt += 1
                m, m_tail = merge(s1,s2)
            else:
                s2 = Node()
                m, m_tail = merge(s1,s2)
            tail.next = m.next
            tail = m_tail

            L.next = res.next
            tail = res
            res.next = None
            if cnt <= 2:
                break
        return L

a = Node()
a.val = "ssss"
pass