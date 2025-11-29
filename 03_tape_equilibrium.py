"""https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/"""

# Time complexity:
# Sum of array is O(N), Single pass with simple math ops is O(N)
# Overall: O(N)

def solution(a: list[int]) -> int:
    """
    Find min abs diff between the first and second
    parts (nonempty) of array split at any position.
    E.g. a = [3,1,2], [3] [1,2] -> |4 - 3| = 1 is one split
    """
    n = len(a)
    total = sum(a)
    res = float('inf')
    left = 0

    for i in range(n - 1):
        left += a[i]
        right = total - left
        cur = abs(left - right)
        res = min(res, cur)

    return res
