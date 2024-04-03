# Mamy daną tablicę stringów, gdzie suma długości wszystkich stringów daje n. Napisz algorytm,
# który posortuje tę tablicę w czasie O(n).

# Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.
import random
import string
from time import time



def count_sort_by(T, x):
    B = [None for _ in range(len(T))]
    C = [0 for _ in range(ord('z') - ord('a')+1)]
    for i in range(len(T)):
        C[ord(T[i][x]) - ord('a')] += 1
    for i in range(1, len(C)):
        C[i] = C[i] + C[i - 1]
    for i in range(len(T) - 1, -1, -1):
        idx = C[ord(T[i][x]) - ord('a')]
        C[ord(T[i][x]) - ord('a')] -= 1
        B[idx - 1] = T[i]
    return B


def strings_sort(T):
    longest = 0
    for el in T:
        longest = max(longest, len(el))
    buckets = [list() for _ in range(longest)]
    for el in T:
        buckets[len(el) - 1].append(el)
    for i in range(longest - 1, 0, -1):
        if len(buckets[i]) > 0:
            buckets[i] = count_sort_by(buckets[i], i)
            buckets[i - 1].extend(buckets[i])
    if len(buckets[0]) > 0:
        buckets[0] = count_sort_by(buckets[0], 0)
    for i in range(len(buckets[0])):
        T[i] = buckets[0][i]

# --------------------------------------------------------

def test_bucket_sort(strings):
    # Inicjalizacja kubełków
    buckets = [[] for _ in range(26)]

    # Rozdzielanie stringów do odpowiednich kubełków na podstawie pierwszej litery
    for string in strings:
        buckets[ord(string[0]) - ord('a')].append(string)

    # Sortowanie każdego kubełka (może to być wykonane rekurencyjnie)
    for bucket in buckets:
        bucket.sort()

    # Łączenie posortowanych kubełków w jedną tablicę wynikową
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


def generate_test(n, max_length):
    strings = []
    total_length = 0
    while total_length < n:
        length = random.randint(1, max_length)
        total_length += length
        if total_length > n:
            length -= total_length - n
        string_value = ''.join(random.choices(string.ascii_lowercase, k=length))
        strings.append(string_value)
    return strings

# Przykład użycia
n = 10000000  # Sumaryczna długość wszystkich stringów
max_length = 1000  # Maksymalna długość pojedynczego stringa
test_input = generate_test(n, max_length)
# --------------------------------------------------------

tab = test_input.copy()


print("2 test---------------")
start = time()
test_bucket_sort(test_input)
print(time() - start)


print("2 bucket---------------")
start = time()
strings_sort(tab)
print(time() - start)


