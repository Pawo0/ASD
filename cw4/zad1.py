def count_sort(A, n, key):
    T = [0 for _ in range(n)]
    for i in range(n):
        T[key(A[i])] += 1
    for i in range(1, n):
        T[i] = T[i - 1]
    A2 = [0 for _ in range(n)]
    for i in range(0, n):
        A2[T[key(A[i])]] = A[i]
        T[key(A[i])] -= 1
    return A2


def radix_sort(A, n):
    A2 = count_sort(A, n, lambda x: x % n)
    A3 = count_sort(A2, n, lambda x: x // n)
    return A3
