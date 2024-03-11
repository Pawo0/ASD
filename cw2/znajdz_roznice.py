# idk man
def find_diff(L, val):
    n = len(L)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if L[i] - L[j] == val:
                return L[i],L[j]
    return None, None

# gąsienica
def find(T,val):
    n = len(T)
    i = 0
    j = 0
    while i<n and j<n:
        if T[i] - T[j] == val:
            return i,j
        elif T[i] - T[j] < val:
            i += 1
        else:
            j += 1
    return None


# połówkowe
def find_diff_better(T,x):
    for i in range(len(T)):
        a = T[i]
        b = a-x
        j = bin_search(T,b)
        if j is not None:
            pass


def bin_search(T,b):
    l = 0
    r = len(T)
    while l != r:
        m = (l+r)//2
        if T[m] == b:
            return m
        elif T[m] < b:
            l = m
        else:
            r = m
        if T[l] == b:
            return l
        else:
            return None

