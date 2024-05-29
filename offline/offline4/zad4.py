from zad4testy import runtests


def Flight(L, x, y, t):
    def dfs(curr, low, high):
        if curr == y:
            return True
        flag_g = False
        for v, e in G[curr]:
            if not vis[v] and high - 2 * t <= e <= low + 2 * t:
                vis[curr] = True
                flag_g = dfs(v, min(low, e), max(high, e)) or flag_g
                vis[curr] = False

                if flag_g:
                    return True
        return False

    v_len = 0
    for el in L:
        v_len = max(el[0], el[1], v_len)
    G = [[] for _ in range(v_len + 1)]
    vis = [False for _ in range(v_len + 1)]
    for el in L:
        G[el[0]].append((el[1], el[2]))
        G[el[1]].append((el[0], el[2]))

    flag = False
    for i, el in enumerate(G[x]):
        vis[i] = True
        flag = dfs(el[0], el[1], el[1]) or flag
        vis[i] = False

        if flag:
            return True
    return False


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(Flight, all_tests=True)
