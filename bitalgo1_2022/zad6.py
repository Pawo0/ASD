# Dana jest tablica z n liczbami całkowitymi. Zawiera ona bardzo dużo powtórzeń - co więcej,
# zaledwie O(log(n)) liczb jest unikatowe (reszta to powtórzenia).
# Napisz algorytm, który w czasie O(n*log(log(n))) posortuje taką tablicę.

from math import log2, ceil
import random
from time import time


def partition(T, l, r):
    x = T[r][0]
    i = l - 1
    for j in range(l, r):
        if T[j][0] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quick_sort(T, l, r):
    while l < r:
        q = partition(T, l, r)
        quick_sort(T, l, q - 1)
        l = q + 1


def bin_search(T, x, l, r):
    # return -1 if x isn't in the list
    while l <= r:
        mid = (l + r) // 2
        if T[mid][0] == x:
            return mid
        elif T[mid][0] > x:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def zad6(T):
    count_unique = [None] * ceil(log2(len(T)))
    curr_len = 0
    for i in range(len(T)):
        idx = bin_search(count_unique, T[i], 0, curr_len - 1)
        if idx == -1:
            count_unique[curr_len] = [T[i], 1]
            quick_sort(count_unique,0,curr_len)
            curr_len += 1
        else:
            count_unique[idx][1] += 1
    i = 0
    for el in count_unique:
        for _ in range(el[1]):
            T[i] = el[0]
            i += 1

# ---------------------------------------------------------------------
def sort_array_with_repeats(arr):
    # Tworzymy słownik, aby zliczyć wystąpienia poszczególnych elementów w tablicy
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # Tworzymy listę unikatowych liczb
    unique_nums = list(count.keys())

    # Sortujemy listę unikatowych liczb używając algorytmu sortowania QuickSort
    test_quicksort(unique_nums, 0, len(unique_nums) - 1)

    # Tworzymy nową posortowaną tablicę, uwzględniając powtórzenia
    sorted_arr = []
    for num in unique_nums:
        sorted_arr.extend([num] * count[num])

    return sorted_arr


# Implementacja algorytmu QuickSort
def test_quicksort(arr, low, high):
    if low < high:
        pi = test_partition(arr, low, high)
        test_quicksort(arr, low, pi - 1)
        test_quicksort(arr, pi + 1, high)


def test_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# ---------------------------------------------------------------------

if __name__ == "__main__":
    n = 2**25
    unique_nums_count = 25
    print("generating test --------")
    start = time()
    arr = [random.randint(1, unique_nums_count) for _ in range(n)]
    arr2 = arr.copy()
    print(time()-start)

    print("test -----------")
    start = time()
    arr2 = sort_array_with_repeats(arr2)
    print(time()-start)

    print("mine ------------")
    start = time()
    zad6(arr)
    print(time() - start)

    print("valid check ---------")
    print(arr == arr2)