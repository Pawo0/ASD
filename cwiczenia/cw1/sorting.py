from random import randint


def bsort(T):
    for i in range(len(T)):
        for j in range(len(T)-i-1):
            if T[j] > T[j+1]:
                T[j],T[j+1] = T[j+1], T[j]


def insert_sort(T):
    for i in range(1,len(T)):
        for j in range(i,0,-1):
            if T[j] < T[j-1]:
                T[j],T[j-1] = T[j-1], T[j]
            else:
                break


def select_sort(T):
    n = len(T)
    for i in range(n):
        idx = i
        for j in range(i,n):
            if T[j] < T[idx]:
                idx = j
        T[i], T[idx] = T[idx],T[i]







tab = [randint(1,100) for _ in range(20)]
print(tab)
bsort(tab)
print(tab)
