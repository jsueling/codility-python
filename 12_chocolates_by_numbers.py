"""https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/"""

# Time complexity:
# GCD computation is O(log(min(N, M)))
# Overall: O(log(min(N, M)))

def solution(n: int, m: int) -> int:
    """
    Return number of chocolates eaten from a circle of N chocolates,
    eating every M-th chocolate until returning to the first chocolate.
    """
    def gcd(a, b):
        if a % b == 0:
            return b
        return gcd(b, a % b)

    # 1. At which index does the first repeat occur?
    #    Assume the first repeat occurs at a non-zero index at step j
    #    after step i, then (i * M) mod N == (j * M) mod N.
    #    In other words, we're at the same index in cycle N.
    #    After subtraction, ((j - i) * M) mod N == 0.
    #    Since we started at index 0, we have discovered a smaller
    #    step K = j - i where we must have visited index 0, as j > i > 0
    #    implies that K > 0. This contradicts our assumption that the
    #    first repeat occurred at step j (a non-zero index).
    #    By contradiction, the first repeat must occur at index 0.

    # 2. Given that the first repetition occurs at index 0,
    #    we need to find the lowest number of steps, K, such that (K * M) mod N == 0.
    #    In other words, the first intersection of the 2 sequences:
    #    [M, 2M, 3M, ...] and [N, 2N, 3N, ...].
    #    This is the definition of the LCM of N and M.

    # 3. Total distance before first intersection = LCM(N, M) = (N * M) / GCD(N, M)
    #    Solve for K, number of steps:
    #    K * M = (N * M) / GCD(N, M)
    #    K = (N * M) / GCD(N, M) / M
    #    K = N / GCD(N, M)

    # 4. The first repeat happens after K steps, therefore K unique
    #    positions are visited (chocolates eaten), return K

    return n // gcd(n, m)
