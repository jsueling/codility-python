"""https://app.codility.com/programmers/lessons/15-caterpillar_method/count_triangles/"""

# Time complexity:
# Precomputation sorting is NlogN
# Nested loop l and r O(N^2)
# For each set l and r, binary search in the range for lowest possible m O(logN)
# Overall O(N^2 logN)

def solution_a(a: list) -> int:
    """
    So close! Fails 3 performance tests
    ▶ large2
    1 followed by an ascending sequence of ~1K elements from [1..2K]
    ✘ TIMEOUT ERROR running time: 0.589 sec., time limit: 0.528 sec.
    ▶ large_random
    chaotic sequence of values from [1..1M], length=1K
    ✘ TIMEOUT ERROR running time: 0.607 sec., time limit: 0.552 sec.
    ▶ large_the_same
    sequence of the same value value
    ✘ TIMEOUT ERROR running time: 0.509 sec., time limit: 0.488 sec.
    """
    n = len(a)
    res = 0
    a.sort()
    def binary_search(l, r):
        """Find lowest m in (l, r) where a[l] + a[m] > a[r], or return -1 if impossible"""
        cand = -1
        lo, hi = l+1, r-1
        while lo <= hi:
            m = (lo+hi)//2
            if a[l] + a[m] > a[r]:
                cand = m
                hi = m - 1
            else:
                lo = m + 1
        return cand
    for r in range(2, n):
        for l in range(r-1):
            m = binary_search(l, r)
            if m == -1:
                continue
            res += r-m
    return res

# Optimised Time complexity:
# Precomputation sorting is O(NlogN)
# Outer loop runs O(N) for l
# Inner loop runs O(2N) for m and r combined, r is bound by n and only increments.
# Overall O(NlogN + N * 2N) = O(N^2)

def solution_b(a: list) -> int:
    """
    15.2. Exercise https://codility.com/media/train/13-CaterpillarMethod.pdf
    Count the number of triangles
    """
    n = len(a)
    res = 0
    a.sort()
    for x in range(n-2):
        z = x + 2
        for y in range(x+1, n-1):
            while z < n and a[x] + a[y] > a[z]:
                z += 1
            res += z-y-1
    return res
