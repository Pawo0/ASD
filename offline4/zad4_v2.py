from zad4testy import runtests


def Flight(L, x, y, t):
    def bfs(curr, vis):
        vis[curr] = True
        q = list()
        q_start, q_end = 0, 0
        for el in G[curr]:
            if el == y: return True
            q.append(el)
            vis[el] = True
            q_end += 1
        while q_start < q_end:
            v = q[q_start]
            q_start += 1
            for el in G[v]:
                if not vis[el]:
                    if el == y: return True
                    q.append(el)
                    vis[el] = True
                    q_end += 1
        for vi in q:
            vis[vi] = False
        return False

    def dfs(curr, vis):
        if curr == y:
            return True
        vis[curr] = True
        for el in G[curr]:
            if not vis[el]:
                if dfs(el, vis):
                    vis[curr] = False
                    return True
        vis[curr] = False
        return False

    v_len = 0
    for el in L:
        v_len = max(el[0], el[1], v_len)
    visit = [False for _ in range(v_len + 1)]
    G = [[] for _ in range(v_len + 1)]
    L = sorted(L, key=lambda el: el[2])
    n = len(L)
    is_x, is_y = 0, 0
    i, j = 0, -1
    while i < n - 1:
        while j < n - 1 and L[j + 1][2] - L[i][2] <= 2 * t:
            G[L[j + 1][0]].append(L[j + 1][1])
            G[L[j + 1][1]].append(L[j + 1][0])
            is_x += 1 if L[j + 1][0] == x or L[j + 1][1] == x else 0
            is_y += 1 if L[j + 1][0] == y or L[j + 1][1] == y else 0
            j += 1

        if is_x and is_y and bfs(x, visit):
            return True

        is_x -= 1 if L[i][0] == x or L[i][1] == x else 0
        is_y -= 1 if L[i][0] == y or L[i][1] == y else 0
        to_del = L[i][0]
        to_del2 = L[i][1]
        G[to_del].remove(to_del2)
        G[to_del2].remove(to_del)
        i += 1

    return False


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(Flight, all_tests=True)


# L = input()
# L = eval(L)
# x = int(input())
# y = int(input())
# t = int(input())
#
# print(Flight(L, x, y, t))
