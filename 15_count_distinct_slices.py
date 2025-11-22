"""https://app.codility.com/programmers/lessons/15-caterpillar_method/count_distinct_slices/"""

# Time complexity:
# Iterating over every possible end-of-slice index r is O(N)
# Start-of-slice index l only increments and cannot pass r, so is O(N) work
# Overall O(2N) = O(N)

def solution(m: int, a: list) -> int:
    """
    All elements of array are integers in range [0..m]
    Count number of slices with no duplicate elements
    """

    limit = 1_000_000_000
    n = len(a)
    seen = [False] * (m + 1)
    res = 0
    l = 0
    for r in range(n):
        # Discarding elements from the left (l) is safe, as any slice
        # (l:k) where r < k < n will also contain a[r], thus invalid
        while seen[a[r]]:
            seen[a[l]] = False
            l += 1
        seen[a[r]] = True
        # Counting the number of slices ending at r with no duplicate elements
        res += r - l + 1
        if res >= limit:
            return limit
    return res
