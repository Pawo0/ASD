# Paweł Czajczyk
# Algorytm to zmodyfikowana Dijkstra, która sprawdza wszystkie możliwe najkrótsze ścieżki, dla
# każdego możliwego poziomu energi. Na koniec zwraca najkrótsza sciezke ze wszystkich końcowych poziomów energii.
# Złożoność O(ElogV)

from kol2testy import runtests
from queue import PriorityQueue


def warrior(G, s, t):
    n = 0
    for i, j, _ in G:
        n = max(n, i, j)
    n += 1
    graf = [[] for _ in range(n)]
    for fr, to, wag in G:
        graf[fr].append((wag, to))
        graf[to].append((wag, fr))

    d = [[float("inf") for _ in range(16+1)] for _ in range(n + 1)]
    q = PriorityQueue()
    d[s][16] = 0
    q.put((0, s, 16))
    while not q.empty():
        dl, u, en = q.get()
        if u == t:
            return dl
        for dl2, v in graf[u]:
            if en - dl2 < 0:
                if d[v][16-dl2] > dl+dl2+8:
                    d[v][16-dl2] = dl+dl2+8
                    q.put((d[v][16-dl2],v,16-dl2))
            else:
                if d[v][en-dl2] > dl + dl2:
                    d[v][en-dl2] = dl + dl2
                    q.put((d[v][en-dl2], v, en - dl2))
    return min(d[t])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(warrior, all_tests=True)
