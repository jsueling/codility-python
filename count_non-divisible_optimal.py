
from collections import Counter

def solution(A):
    N = len(A)
    if N == 0:
        return []
    M = max(A)
    counts = Counter(A)
    divisor_counts = [0] * (M + 1)
    for i in range(1, M + 1):
        if counts[i] > 0:
            for j in range(i, M + 1, i):
                divisor_counts[j] += counts[i]
    result = []
    for num in A:
        non_divisors = N - divisor_counts[num]
        result.append(non_divisors)
    return result
