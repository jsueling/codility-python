"""https://app.codility.com/programmers/lessons/12-euclidean_algorithm/common_prime_divisors/"""

# I translated the algorithm from: https://stackoverflow.com/a/34252571

# Time complexity:
# Let Z = length of arrays A and B
# Let C = max(A[i], B[i] for all i in [0..Z-1])
# each element of arrays A and B is an integer within the range [1..2,147,483,647].
# GCD computation of numbers D, E is is O(log(min(D, E)))
# Overall: O(Z * log(C))

def solution(a: list, b: list) -> int:
    """Count number of positions i where a[i] and b[i] have the same prime divisors"""

    def gcd(a, b):
        if a % b == 0:
            return b
        return gcd(b, a % b)

    def common_prime_divisors(x, y):
        """
        Both x and y must be factorisable using only the common set of prime factors of
        the original gcd for them to have the same common prime divisors.
        """
        if x == 1 and y == 1:
            return 1
        if x == 1 or y == 1:
            return 0
        # Find common set of product of prime factors of x and y
        # E.g. common_prime_divisors(15, 75)
        # prime_factors(15) = {3, 5}, prime_factors(75) = {3, 5, 5}
        # Common set of prime factors (gcd) of 15 and 75 is {3, 5}
        cur = gcd(x, y)
        tmp = cur
        if cur == 1:
            return 0
        while True:
            # Reduce x by the product of the common set of prime factors
            x //= cur
            # If x can be factorised only by the common set of prime factors, success
            if x == 1:
                break
            # Reduce the common set of prime factors to those remaining in x
            cur = gcd(x, cur)
            # x has a prime factor not in the common set of prime factors
            if cur == 1:
                return 0
        # Repeat for y
        while True:
            y //= tmp
            if y == 1:
                return 1
            tmp = gcd(y, tmp)
            if tmp == 1:
                return 0

    return sum(common_prime_divisors(a[i], b[i]) for i in range(len(a)))
