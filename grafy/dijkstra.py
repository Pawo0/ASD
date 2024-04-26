from queue import PriorityQueue


class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], src: int) -> dict[int, int]:
        G = [[] for _ in range(n)]
        for fr, to, wag in edges:
            G[fr].append((to, wag))

        d = {i: -1 for i in range(n)}
        d[src] = 0
        q = PriorityQueue()
        q.put((0, src))
        while not q.empty():
            dl, u = q.get()
            for v, dl2 in G[u]:
                if d[v] == -1 or d[v] > dl + dl2:
                    d[v] = dl + dl2
                    q.put((dl + dl2, v))
        return d


s = Solution()
t = [[0, 1, 5], [0, 2, 7], [1, 2, 2], [1, 3, 6], [2, 3, 4]]
print(s.shortestPath(4, t, 1))
