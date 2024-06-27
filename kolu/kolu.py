# jakas taka upo wzorcowka, bfs ze zliczaniem co ile "nowa seria" wierzchołkow

from kolutesty import runtests
from collections import deque


def projects(n, L):
    g = [[] for _ in range(n)]
    can_vis = [0 for _ in range(n)]
    for to, fr in L:
        g[fr].append(to)
        can_vis[to] += 1
    q = deque()
    for i, cn in enumerate(can_vis):
        if cn == 0:
            q.append(i)
    cnt = 1
    l = len(q)
    while len(q) > 0:
        v = q.popleft()
        l -= 1
        for el in g[v]:
            can_vis[el] -= 1
            if can_vis[el] == 0:
                q.append(el)
        if len(q) and l == 0:
            cnt += 1
            l = len(q)
    return cnt


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(projects, all_tests=True)
