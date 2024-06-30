# Paweł Czajczyk
# złożoność ElogV
# Na początku przykształcam graf na liste sąsiedztwa, oraz ze wszystkich rowerow dla kazdego wierzchołka
# wybieram najlepszy
# Robię tablice odleglosci dla kazdego wierzcholka z minimalnym kosztem
# Uzywam algorytmu Dijkstra od tyłu, gdy dojde do wierzchołka gdzie jest rower aktualizuje odleglosc,
# ze jesli to co przeszedlem pieszo * (p/q) jest lepesze to aktualizuje. Podobnie dla najlepszego wczesniej
# roweru + przejscie pieszo, albo po prostu przejscie calosci pieszo
# Na koniec zwracam minimalna wartosc z poczatkowego wierzchołka spośród przejscia pieszo i z uzyciem najlepszego
# roweru


from egz1atesty import runtests
# from queue import PriorityQueue
from heapq import heappush, heappop
from math import inf, floor


def armstrong(B, G, s, t):
    n = 0
    for i, j, _ in G:
        n = max(n, i, j)
    n += 1
    graph = [[] for _ in range(n)]
    bikes = [[inf, 1] for _ in range(n)]
    for i, j, val in G:
        graph[i].append([val, j])
        graph[j].append([val, i])
    for i, p, q in B:
        if p / q < bikes[i][0] / bikes[i][1]:
            bikes[i][0] = p
            bikes[i][1] = q

    d = [[inf for _ in range(2)] for _ in range(n + 1)]  # z rowerem i bez
    # q = PriorityQueue()
    q = []
    d[t][0] = 0
    # q.put((0, 0, inf, t))
    heappush(q,(0, 0, inf, t))

    # while not q.empty():
    while q:
        # m, dl_p, dl_r, u = q.get()
        m, dl_p, dl_r, u = heappop(q)
        for dl2, v in graph[u]:
            flag = False
            if bikes[v][0] < inf: # jesli jest rower
                if d[v][1] > (dl_p + dl2) * (bikes[v][0] / bikes[v][1]): # jest przejechanie z rym rowerem jest lepsze niz z jakims poprzednim
                    d[v][1] = (dl_p + dl2) * (bikes[v][0] / bikes[v][1])
                    flag = True
            if dl_r+dl2 < d[v][1]: # jesli najlepsze uzycie poprszedniego roweru
                d[v][1] = dl_r + dl2
                flag = True

            if d[v][0] > dl_p + dl2: # jesli przejscie pieszo lepsze od poprzedniego
                d[v][0] = dl_p + dl2
                flag = True
            if flag:
                # q.put((min(d[v][0], d[v][1]), d[v][0], d[v][1], v))
                heappush(q,(min(d[v][0], d[v][1]), d[v][0], d[v][1], v))
    return floor(min(d[s]))


# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests(armstrong, all_tests=True)
G = [[0, 1, 2], [0, 2, 3], [1, 3, 2], [2, 3, 20], [3, 4, 100]]
B = [[1, 1, 2], [2, 1, 10]]
s = 0
t = 4
print(armstrong(B,G,s,t))