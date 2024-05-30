from zad5testy import runtests
from queue import PriorityQueue


def spacetravel(n, E, S, a, b):
    G = [[] for _ in range(n + 1)]
    for fr, to, wag in E:
        G[fr].append((wag, to))
        G[to].append((wag, fr))
    for i in S:
        G[n].append((0, i))
        G[i].append((0, n))

    d = [float("inf") for _ in range(n + 1)]
    q = PriorityQueue()
    d[a] = 0
    q.put((0, a))
    while not q.empty():
        dl, u = q.get()
        if u == b:
            return dl
        for dl2, v in G[u]:
            if d[v] > dl + dl2:
                d[v] = dl + dl2
                q.put((d[v], v))
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
