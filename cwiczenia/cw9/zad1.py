def points(x):
    cnt = 0
    n = len(x)
    x.sort()
    start = x[0]
    for i in range(1, n):
        if x[i] > x[start] - 1:
            pass
        else:
            cnt += 1
            start = x[i]
    return cnt
