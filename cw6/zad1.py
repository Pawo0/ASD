def euler(G):
    cycle = []
    n = len(G)
    idx = [0 for _ in range(n)]

    def dfs(G,v):
        nonlocal cycle, n
        while idx[v] < n:
            i = idx[v]
            idx[v] += 1
            if G[v][i] == 1:
                G[v][i] = 0
                G[i][v] = 0
                dfs(G,i)
        cycle.append(v)
    dfs(G,0)
