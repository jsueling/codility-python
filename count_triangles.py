# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

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
    def binary_search(l1, r1):
        cand = r1
        l2, r2 = l1+1, r1
        while l2 <= r2:
            m = (l2+r2)//2
            if a[l1] + a[m] > a[r1]:
                cand = m
                r2 = m - 1
            else:
                l2 = m + 1
        return cand
    for r in range(2, n):
        for l in range(r-1):
            m = binary_search(l, r)
            if m == r:
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
    Credits to johnmee's solution:
    https://github.com/johnmee/codility/blob/master/15_CountTriangles.py
    """
    n = len(a)
    res = 0
    a.sort()
    for l in range(n-2):
        r = l + 2
        for m in range(l+1, n-1):
            while r < n and a[l] + a[m] > a[r]:
                r += 1
            res += r-m-1
    return res
