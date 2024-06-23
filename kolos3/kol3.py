# Paweł Czajczyk
# złożoność n^2
# tablica f[i][j] = ile drzew od 0 do i trzeba wyciąć, żeby modulo pozostałych drzew wynosiło j
# dla kazdego i oraz j ustala aktualna najmniejsza, albo "ilosc drzew wyciatych zeby otrzymac ten wynik j"
# z f[i-1][j] (czyli uwzgedniajac do drzewa wczesniej)
# oraz dla kazdej poprzedniej "najmniejszej ilosci wycietych drzew do otrzymania konretnego wyniku j" przepisujemy
# do kolejnego indeksu i, gdzie j to (j + T[i] )%m


from kol3testy import runtests
from math import inf


def orchard(T, m):
    n = len(T)
    f = [[inf for _ in range(m)] for _ in range(n)]
    for i in range(n):
        f[i][0] = i + 1
    f[0][T[0] % m] = 0
    for i in range(1, n):
        for j in range(m):
            f[i][j] = min(f[i - 1][j] + 1, f[i][j])
            f[i][(j + T[i]) % m] = min(f[i][(j + T[i]) % m], f[i - 1][j])
    return f[-1][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)