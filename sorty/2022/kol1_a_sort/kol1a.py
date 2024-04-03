from kol1atesty import runtests


def count_sort_by(T, by):
    res = [None] * len(T)
    C = [0] * (ord('z')-ord('a')+1)
    for item in T:
        idx = ord(item[by])-ord('a')
        C[idx] += 1
    for i in range(1,len(C)):
        C[i] = C[i-1] + C[i]
    for i in range(len(T)-1,-1,-1):
        idx = ord(T[i][by])-ord('a')
        res[C[idx]-1] = T[i]
        C[idx] -= 1
    for i in range(len(T)):
        T[i] = res[i]


def radix_sort(T, n):
    for i in range(n - 1, -1, -1):
        count_sort_by(T, i)


def g(T):
    max_len = 0
    min_len = float('inf')
    for i in range(len(T)):
        max_len = max(max_len, len(T[i]))
        min_len = min(min_len, len(T[i]))
        if T[i][0] > T[i][-1]:
            T[i] = T[i][::-1]
    buckets = [list() for _ in range(max_len - min_len + 1)]
    for el in T:
        buckets[len(el) - min_len].append(el)

    i = min_len
    res = 0
    for bucket in buckets:
        radix_sort(bucket,i)
        i += 1
        if len(bucket) > res:
            last = bucket[0]
            cnt = 0
            for el in bucket:
                if last == el:
                    cnt += 1
                else:
                    res = max(cnt,res)
                    last = el
                    cnt = 1
            res = max(cnt, res)

    return res


# tab = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
# g(tab)
# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests(g, all_tests=True)
