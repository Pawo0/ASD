# a)
def traktor(x,L,b,a=0):
    start = a
    cnt = 0
    while start < b:
        n_start = start
        for i in range(L):
            if start + i == b:
                return cnt
            if x[start + i] == "fuel":
                n_start = start + i
        if n_start == start:
            return False
        start = n_start
        cnt += 1
    return cnt
t = ["fuel", "empty", "fuel", "empty", "fuel"]
print(traktor(t,3,5,))

