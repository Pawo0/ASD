from zad6testy import runtests
from math import inf


def jumper(G, s, w):
    n = len(G)
    vis_n = [False for _ in range(n)]
    d_n = [inf for _ in range(n)]
    d_d = [inf for _ in range(n)]
    vis_d = [False for _ in range(n)]
    d_n[s] = 0
    for _ in range(n):
        min_idx = inf
        min_dl = inf
        # normalne
        for v in range(n):
            if not vis_n[v] and d_n[v] < min_dl:
                min_dl = d_n[v]
                min_idx = v
        if min_idx != inf:
            vis_n[min_idx] = True
            for u, dl in enumerate(G[min_idx]):
                # z normalnego na normalne
                if dl != 0 and dl + d_n[min_idx] < d_n[u]:
                    d_n[u] = dl + d_n[min_idx]
                    vis_n[u] = False
                # z normalnego na podwojne
                if dl != 0:
                    for u2, dl2 in enumerate(G[u]):
                        if dl2 != 0 and max(dl, dl2) + d_n[min_idx] < d_d[u2]:
                            d_d[u2] = max(dl, dl2) + d_n[min_idx]
                            vis_d[u2] = False
        # podwojne
        min_idx = inf
        min_dl = inf
        for v in range(n):
            if not vis_d[v] and d_d[v] < min_dl:
                min_dl = d_d[v]
                min_idx = v
        if min_idx != inf:
            vis_d[min_idx] = True
            for u, dl in enumerate(G[min_idx]):
                # z podwojnego na normalne
                if dl != 0 and dl + d_d[min_idx] < d_n[u]:
                    d_n[u] = dl + d_d[min_idx]
                    vis_n[u] = False

    return min(d_n[w], d_d[w])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(jumper, all_tests=True)
