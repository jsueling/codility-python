"""https://app.codility.com/programmers/lessons/14-binary_search_algorithm/min_max_division/"""

# Time complexity:
# Binary search over the range (r-l),
# where r is sum(A) and l is max(A) = O(log(M * N))
# Each search step does a linear scan of the array = O(N)
# Overall = O(N log(M * N))

def solution(k: int, m: int, a: list[int]) -> int:
    """
    Find smallest maximum block sum after splitting array into k contiguous blocks,
    no element greater than m, n elements in array a.
    """
    n = len(a)

    def can_div(large_sum: int) -> bool:
        """can div array A into K blocks each with sum of at most large_sum"""
        cur_sum = 0
        blocks = 1
        # Greedily form blocks, packing in the most elements possible
        # as that gives the best chance of keeping the number of blocks low.
        for i in range(n):
            if cur_sum + a[i] > large_sum:
                blocks += 1
                cur_sum = a[i]
                if blocks > k:
                    return False
            else:
                cur_sum += a[i]
        return blocks <= k

    # The bounds for the search:
    # no block can have sum less than the largest element,
    # or more than the sum of all elements.
    l, r = float("-inf"), 0
    for i in range(n):
        l = max(l, a[i])
        r += a[i]

    res = r
    while l <= r:
        m = (l+r)//2
        # If we can divide array into K blocks with max block sum m,
        # search for a smaller maximum block sum.
        if can_div(m):
            res = m
            r = m - 1
        else:
            l = m + 1
    return res
