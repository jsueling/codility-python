"""https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/"""

# Time complexity:
# Initialise array of size N is O(N)
# Single pass with O(1) array ops is O(N),
# Overall: O(N)

def solution(a: list[int]) -> int:
    """
    Return 1 if array A is a permutation or 0 if not.
    A permutation is a sequence containing each element from 1 to N once, and only once.
    """
    n = len(a)
    cnt = [0] * n
    # Each element of array A is an integer within the range [1..1,000,000,000].
    for i in range(n):
        if a[i] > n or cnt[a[i] - 1]:
            return 0
        cnt[a[i] - 1] = 1
    # Exiting the loop verifies that each element A[i] was in range [1..N] and not duplicated
    return 1
