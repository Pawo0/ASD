# Mamy dane n punktów (x, y) w okręgu o promieniu k (liczba naturalna), tzn. 0 <= x2 + y2 <= k,
# które są w nim równomiernie rozłożone, tzn. prawdopodobieństwo znalezienia punktu na danym obszarze
# jest proporcjonalne do pola tego obszaru.
# Napisz algorytm, który w czasie Θ(n) posortuje punkty po ich odległości do punktu (0, 0), tzn.
# d = sqrt(x^2 + y^2).
from math import sqrt
from time import time
import random


def generuj_punkty(n, k):
    punkty = []
    i = 0
    while i < n:
        x = random.randint(-k, k)
        y = random.randint(-k, k)
        if x ** 2 + y ** 2 <= k ** 2:
            punkty.append((x, y))
            i += 1;
    return punkty


def bin_search(T, x, l, r):
    while l < r:
        mid = (l + r) // 2
        if T[mid] == x:
            return mid
        elif T[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return l - 1


def count_d(x):
    return sqrt(x[0] ** 2 + x[1] ** 2)


def insert_sort(T):
    for i in range(0, len(T)):
        min_id = i
        for j in range(i + 1, len(T)):
            if count_d(T[j]) < count_d(T[min_id]):
                min_id = j
        T[i], T[min_id] = T[min_id], T[i]


def sort_by_distance(T, n, k):
    buckets = [list() for _ in range(n)]
    idx = [0]
    for i in range(1, n):
        idx.append(sqrt(k ** 2 / n + idx[i - 1] ** 2))
    for cord in T:
        d = count_d(cord)
        which_bucket = bin_search(idx, d, 0, len(idx))
        buckets[which_bucket].append(cord)
    i = 0
    while i < n:
        for bucket in buckets:
            insert_sort(bucket)
            for el in bucket:
                T[i] = el
                i += 1


def partition(T, l, p):
    q = count_d(T[p])
    i = l
    for j in range(l, p):
        if count_d(T[j]) < q:
            T[i], T[j] = T[j], T[i]
            i += 1
    T[p], T[i] = T[i], T[p]
    return i


def quick_sort(T, l, p):
    while l <= p:
        q = partition(T, l, p)
        quick_sort(T, l, q - 1)
        l = q + 1


def merge(T, t1, t2):
    i, j, k = 0, 0, 0
    while i < len(t1) and j < len(t2):
        if count_d(t1[i]) <= count_d(t2[j]):
            T[k] = t1[i]
            k += 1
            i += 1
        else:
            T[k] = t2[j]
            k += 1
            j += 1
    while i < len(t1):
        T[k] = t1[i]
        k += 1
        i += 1
    while j < len(t2):
        T[k] = t2[j]
        k += 1
        j += 1


def merge_sort(T):
    if len(T) > 1:
        mid = len(T) // 2
        t1 = T[:mid]
        t2 = T[mid:]
        merge_sort(t1)
        merge_sort(t2)
        merge(T, t1, t2)


print("Generating points...")
start = time()
punkty = generuj_punkty(1000000, 100000000)
punkty2 = punkty.copy()
punkty3 = punkty.copy()
print(time() - start)

print("1 sorted---------------")
start = time()
posortowane_oczekiwane = sorted(punkty, key=lambda punkt: punkt[0] ** 2 + punkt[1] ** 2)
print(time() - start)
print("2 bucket---------------")
start = time()
sort_by_distance(punkty, len(punkty), 100000000)
print(time() - start)
print("3 quick---------------")
start = time()
quick_sort(punkty2, 0, len(punkty2) - 1)
print(time() - start)
print("3 merge---------------")
start = time()
merge_sort(punkty3)
print(time() - start)

# print(posortowane_oczekiwane)
# print(punkty)
# print(punkty2)
# print(punkty3)
