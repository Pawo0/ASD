from kol2testy import runtests
from collections import deque

def beautree(G):
    def dfs(v, vis, chk):
        nonlocal cnt
        vis[v] = chk
        for u, wag in G[v]:
            if m <= wag <= M and vis[u] != chk:
                cnt += 1
                dfs(u, vis, chk)

    n = len(G)
    E = []
    for i in range(n):
        for j, w in G[i]:
            if i < j:
                E.append((w, i, j))
    E = sorted(E)

    # print(E)
    visited = [-1 for _ in range(n)]
    for i in range(len(E) - n + 1):
        cnt = 0
        m = E[i][0]
        M = E[i + n - 2][0]
        dfs(E[i][1], visited, i)
        if cnt == n - 1:
            return sum(w for w, _, _ in E[i:i + n - 1])

    return None

#
#   def dfs(self, heights, curr, h, reachabble):
#         x = curr[0]
#         y = curr[1]
#         reachabble[x][y] = True
#         for i, j in self.dest:
#             if 0 <= x+i < len(heights) and 0 <= y+j < len(heights[0]) and heights[x+i][y+j] >= h and not reachabble[x+i][y+j]:
#                 self.dfs(heights,(x+i,y+j), max(h,heights[x+i][y+j]),reachabble)
#
#
# def bfs(self, grid, rotten):
#     q = deque()
#     res = 0
#     for v in rotten:
#         self.add_to_queue(grid, q, v[0] - 1, v[1], 1)
#         self.add_to_queue(grid, q, v[0] + 1, v[1], 1)
#         self.add_to_queue(grid, q, v[0], v[1] - 1, 1)
#         self.add_to_queue(grid, q, v[0], v[1] + 1, 1)
#
#     while len(q) != 0:
#         v = q.popleft()
#         res = max(res, v[2])
#         self.add_to_queue(grid, q, v[0] - 1, v[1], v[2] + 1)
#         self.add_to_queue(grid, q, v[0] + 1, v[1], v[2] + 1)
#         self.add_to_queue(grid, q, v[0], v[1] - 1, v[2] + 1)
#         self.add_to_queue(grid, q, v[0], v[1] + 1, v[2] + 1)
#
#     for x in grid:
#         for y in x:
#             if y == 1:
#                 return -1
#     return res
#
#
# def add_to_queue(self, grid, q, i, j, dl):
#     if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
#         grid[i][j] += 1
#         q.append((i, j, dl))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(beautree, all_tests=True)
