# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, M, A):
    n = len(A)
    # K number of blocks
    # no element greater than M, irrelevant
    # smallest maximum sum
    def can_div(large_sum):
        """can div array A into K blocks each with sum of at most large_sum"""
        cur_sum = 0
        blocks = 1
        for i in range(n):
            if cur_sum + A[i] > large_sum:
                blocks += 1
                cur_sum = A[i]
                if blocks > K:
                    return False
            else:
                cur_sum += A[i]
        return blocks <= K
    l, r = float("-inf"), 0
    for i in range(n):
        l = max(l, A[i])
        r += A[i]
    res = r
    while l <= r:
        m = (l+r)//2
        if can_div(m):
            res = m
            r = m - 1
        else:
            l = m + 1
    return res