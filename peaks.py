def solution(A):
    factors = []
    n = len(A)
    i = 1
    while i * i <= n:
        q, r = divmod(n, i)
        if r == 0:
            factors.extend([q, i])
        i += 1
    factors.sort()
    peaks = []
    for i in range(1, n-1):
        if A[i-1] < A[i] > A[i+1]:
            peaks.append(i)
    def can_div(index):
        num_blocks = factors[index]
        i = 0
        j = 0
        block_size = n // num_blocks
        while True:
            i += block_size
            old_j = j
            while j < len(peaks) and peaks[j] < i:
                j += 1
            if old_j == j:
                return num_blocks == 0
            num_blocks -= 1
    for i in range(len(factors)-1,-1,-1):
        if can_div(i):
            return factors[i]
    return 0
    # # Binary search was incorrect
    # l, r = 0, len(factors)-1
    # res = 0
    # while l <= r:
    #     m = (l+r) // 2
    #     if can_div(m):
    #         res = factors[m]
    #         l = m + 1
    #     else:
    #         r = m - 1
    # return res