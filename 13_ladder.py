"""https://app.codility.com/programmers/lessons/13-fibonacci_numbers/ladder/"""

# Time complexity:
# M is max value in A (max ladder size/rungs) and N is length of A
# Fib(M) is O(M), then O(N) lookups
# Overall: O(N + M)

def solution(a: list, b: list) -> list:
    """
    Climb 1 or 2 rungs at a time.
    I.e. add numWays(i-1) + numWays(i-2) to get numWays(i) which is the fib function.
    Count ways to climb ladders of a[i] sizes mod 2^b[i].
    """
    n = len(a)
    m = max(a)
    max_b = max(b)
    limit = 1 << max_b

    # dp[i] = number of ways to climb ladder of size i
    dp = [0] * (m + 1)
    # 1 way to climb a ladder of rung size 0 or 1
    dp[0] = dp[1] = 1

    for i in range(2, m + 1):
        # Fib grows exponentially, so mod by limit to reduce work done,
        # as addition of numbers below 2 ** 30 is O(1) and 0 <= b[i] <= 30.
        # Does not affect correctness of final result as
        # binary modulo chops off higher bits that we don't need.
        # I.e. mod by a smaller power of 2 removes same higher bits as mod by a larger power of 2.
        dp[i] = (dp[i - 1] + dp[i - 2]) % limit

    return [dp[a[i]] % (1 << b[i]) for i in range(n)]
