"""https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/count_factors/"""

# Time complexity:
# O(1) check for each possible factor, up to sqrt(N) factors
# since we can find the complement factor n / i
# Overall: O(sqrt(N))

def solution(n: int) -> int:
    """Count the number of factors of n"""
    i = 1
    res = 0
    while i * i <= n:
        q, r = divmod(n, i)
        if r == 0:
            # Each factor has an additional complement n / i, except for perfect squares
            res += 2 if q != i else 1
        i += 1
    return res
