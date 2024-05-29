from math import inf

def dijkstra(G,s):
    n = len(G)
    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    d[s] = 0
    while True:
        mini = inf
        u = inf
        for e in range(n):
            if e < mini and not visited[e]:
                mini = d[e]
                u = e
        if u == inf:
            break
        visited[u] = True
        for i in range(n):
            if G[u][i] < inf and d[i] > d[u] + G[u][i]:
                d[i] = d[u] + G[u][i]
                parent[i] = u
    return d, parent
