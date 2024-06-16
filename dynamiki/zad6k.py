from zad6ktesty import runtests


def haslo(S):
    print(S)
    n = len(S)
    if n == 0:
        return 1
    f = [0 for _ in range(n + 1)]
    f[0] = 1
    f[-1] = 1
    for i in range(1, n):
        if int(S[i]) == 0 and (int(S[i - 1]) >= 3 or int(S[i - 1] == 0)):
            return 0
        if 10 <= int(S[i-1:i+1]) <= 26:
            f[i] += f[i - 2]
        if S[i] != '0':
            f[i] += f[i - 1]
    return f[n - 1]


runtests(haslo)
