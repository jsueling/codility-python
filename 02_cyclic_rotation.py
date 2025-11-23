"""https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/"""

# Time complexity:
# Slice array into two parts and concatenate them, each taking O(N) time per op
# Overall = O(N)

def solution(a: list[int], k: int) -> list[int]:
    """Rotate array A to the right K times."""
    n = len(a)
    if n == 0:
        return a
    k = k % n  # if K is greater than N
    return a[-k:] + a[:-k]
