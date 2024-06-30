# Paweł Czajczyk
# Złożoność k^2*n^2*logn, ale raczej dziala
# Bruteforce dla kazdego mozliwego przedzialu odejmuje  od 0 do k najmniejszych liczb i wybiera
# najwieksza wartosc

from egz1btesty import runtests
from heapq import nsmallest, heappush


def kstrong(T, k):
    n = len(T)
    res = 0
    for i in range(n):
        suma = 0
        q = []
        for j in range(i, n):
            suma += T[j]
            heappush(q,T[j])
            for l in range(k+1):
                res = max(res,suma - sum(nsmallest(l,q)))

    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kstrong, all_tests=True)