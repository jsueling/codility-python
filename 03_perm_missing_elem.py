"""https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/"""

# Time complexity:
# Sum requires single pass which is O(N), other math ops are O(1)
# Overall: O(N)

def solution(a: list[int]) -> int:
    """
    An array A consisting of N different integers is given.
    The array contains integers in the range [1..(N + 1)],
    which means that exactly one element is missing.
    - find missing element
    """
    n = len(a)
    # formula for arithmetic progression sum
    expected_sum = (n+1) * (n + 2) // 2
    actual_sum = sum(a)
    return expected_sum - actual_sum
