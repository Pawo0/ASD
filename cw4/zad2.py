def bin_search(array, value):
    left, right = 0, len(array)
    while left:
        mid = (left + right) // 2
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            right = mid - 1
        else:
            left = mid + 1


def counting_sort(A):
    n = len(A)
    vals = unique_vals(A, n)
    counts = [0 for i in range(len(vals))]
    for x in A:
        idx = bin_search(vals, x)
        counts[idx] += 1
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]


def unique_vals(A, n):
    vals = []
    for x in A:
        if not bin_search(vals, x):  # O(n*log(log(n)))
            # instert(vals, x) // binsearcher
            pass
    return vals
