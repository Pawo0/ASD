from zad3ktesty import runtests


def ksuma(T, k):
    n = len(T)
    f = [float('inf') for _ in range(n)]
    f[0] = T[0]
    for i in range(1,n):
        j = 1
        m = float('inf')
        while i - j >= 0 and j <= k:
            m = min(m,f[i-j])
            j += 1
        if j < k:
            m = 0
        f[i] = m + T[i]
    return min(f[-k:])


runtests(ksuma)
