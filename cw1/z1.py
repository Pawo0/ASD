# zlozonosc 3/2n. znajdz max i min

def minmax(T): # pierwsza wersja, trzeba zoptymalizowac jakos
    minimun = T[0]
    maksimum = T[0]
    for x in T:
        if x > maksimum:
            maksimum = x
        elif x < minimun:
            minimun = x

    return minimun, maksimum


# najdluzszy podciag sumujacy sie parzyscie

def tab_sums(T):
    n = len(T)
    sp = [None] * (n+1)
    sp[0] = 0
    s = 0
    for i in range(n):
        s += T[i]
        sp[i+1] = s
    return sp

def func(T):
    n = len(T)
    cnt = 0
    sp = tab_sums(T)
    for i in range(1,n+1):
        for j in range(0,i):
            if (sp[i]-sp[j]) % 2 == 0:
                cnt+=1

# idk przepisze se

def search(T,x):
    i = 0
    j = len(T) - 1
    while (T[i]+T[j]) != 0 and i < j:
        if T[i] + T[j] > x:
            j -= 1
        elif T[i]+T[j] < x:
            i += 1
        else:
            return i,j
        return None,None



# tez w sumie nie wiem, przepisze se

def min_excluded(T):
    if T[0] != 0:
        return 0
    for i in range(len(T)-1):
        if abs(T[i]-T[i+1]) > 1:
            return T[i]+1
        return T[len(T)-1]+1

# ver 2 tego co wyzej


def min_excluded_better(T):
    l, r = T[0], T[len(T) - 1] + 1
    m = 0
    while l < m:
        m = (l + r) // 2
        if T[m] == m:
            l = m
        else:
            r = m
    if T[m+1]-T[m]>1:
        return T[m]+1
""" 
    if l == len(T)-1 and T[len(T)-1] == len(T)-1:
        return len(T)
    return T[l-1]+1
"""