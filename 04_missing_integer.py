"""https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/"""

# Time complexity:
# Init array of size N is O(N)
# 2 single passes with O(1) array ops (set/get) is O(N),
# Overall: O(N)

def solution(a: list[int]) -> int:
    """
    Return the smallest positive integer that does not occur in A.
    A is an array of N integers.
    """
    n = len(a)
    # We observe that the missing integer must be in the range [1..N+1],
    # since there are only N numbers
    present = [False] * (n + 1)
    for val in a:
        if 1 <= val <= n:
            present[val] = True
    for i in range(1, n + 1):
        if not present[i]:
            return i
    return n + 1 # all integers 1..N are present
