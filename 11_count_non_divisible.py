"""https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/count_non_divisible/"""

from math import sqrt, floor
from collections import Counter

# Time Complexity:
# Precompute freqency count of each element in A = O(N)
# Each element in A in range [1, 100_000], let M be the max element in A
# Outer loop: iterate over M counts = O(M)
# Inner loop: for each element iterate over possible divisors = O(sqrt(M))
# Return result for each element in A = O(N)
# Overall: O(2 * N + M * sqrt(M)) = O(N + M * sqrt(M))

def solution_a(a: list[int]) -> list[int]:
    """
    For each element in array A, count the number of elements
    of A (including self) that don't divide the element.
    
    First attempt: Directly count divisors for each unique element.
    Codility score: 88%, failing performance tests
    """

    count_lookup = Counter(a)
    non_divisible_count = Counter()
    n = len(a)
    for element in count_lookup:
        divisor_count = 0
        for divisor in range(1, floor(sqrt(element)) + 1):
            q, r =  divmod(element, divisor)
            if r == 0:
                divisor_count += count_lookup[divisor]
                if q != divisor:
                    divisor_count += count_lookup[q]
        # Non-divisors can be found implicitly through divisors
        num_non_divisor = n - divisor_count
        non_divisible_count[element] = num_non_divisor

    return [non_divisible_count[a[i]] for i in range(n)]

# Time Complexity:
# Precompute freqency count of each element in A = O(N)
# Each element in A in range [1, 100_000], let M be the max element in A
# Outer loop: iterate over M counts = O(M)

# Inner loop: When M is 1, does M/1 work. When M is 2, does M/2 work.
# Across all M iterations, work done is:
# M/1 + M/2 + M/3 + ... + M/M = M * (1 + 1/2 + 1/3 + ... + 1/M).
# The bracketed terms are approximated by the harmonic series which is O(log M),
# so the inner loop does total work = O(M log M).
# Overall: O(N + M + M log M) = O(N + M log M)

def solution_b(a: list[int]) -> list[int]:
    """Optimised solution using the sieve of eratosthenes."""
    if not a:
        return []

    n = len(a)
    m = max(a)

    # Freq count of each number in A
    counts = [0] * (m + 1)
    for num in a:
        counts[num] += 1

    # Number of divisors for each number in A
    divisor_counts = [0] * (m + 1)

    for divisor in range(1, m + 1):
        if counts[divisor] > 0:
            k = divisor
            while k <= m:
                divisor_counts[k] += counts[divisor]
                k += divisor

    return [n - divisor_counts[num] for num in a]
