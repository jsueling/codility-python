"""https://app.codility.com/programmers/lessons/15-caterpillar_method/min_abs_sum_of_two/"""

# Time complexity:
# Precomputation sorting is O(NlogN)
# Two pointer traversal is O(N)
# Overall O(NlogN + N) = O(NlogN)

def solution(a: list) -> int:
    """Sort + Two pointer approach"""
    n = len(a)
    a.sort()
    # -10, -8, 3, 4, 5
    # Always move the pointers greedily, such that the sum moves closer to 0.
    # E.g. l at -10, r at 5, a[l] + a[r] is negative, increment l
    # Will pairing -10 with any smaller number (by decrementing r) be closer to 0?
    # for any j where l < j < r, a[l] + a[j] < a[l] + a[r], i.e. always more negative
    # E.g. l at 3, r at 5, a[l] + a[r] is positive, decrement r
    # Will pairing 5 with any larger number (by incrementing l) be closer to 0?
    # for any i where l < i < r, a[i] + a[r] > a[l] + a[r], i.e. always more positive
    l, r = 0, n-1
    res = float("inf")
    while l <= r:
        cur = a[l] + a[r]
        res = min(res, abs(cur))
        if cur > 0:
            r -= 1
        else:
            l += 1
    return res
