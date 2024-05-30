from collections import deque

# a
def biparted(G):
    visited = [0 for _ in range(len(G))]
    def dfs(v,c):
        nonlocal visited
        visited[v] = c
        for w in G[v]:
            if visited[w] == c:
                return False
            if visited[w] == 0:
                res = dfs(w,-1*c)
                if not res:
                    return False
        return True
    flag = True
    for i in range(len(G)):
        for j in range(len(G[i])):
            if visited[G[i][j]] == 0:
                flag = dfs(G[i][j],1)
    return flag

# b
def cycle(G):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    q = deque()
    q.append(0)
    visited[0] = True
    while q:
        s = q.popleft()
        for i in range(n):
            if G[s][i] == 1 and visited[i] and parent[s] != i:
                return True
            visited[i] = True
            parent[i] = s
            q.append(i)
    return False


G = [[2, 3], [3, 4], [0], [0, 1], [1]]
print(biparted(G))