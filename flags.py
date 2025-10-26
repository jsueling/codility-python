def solution(A):
    n = len(A)
    peaks = []
    for i in range(1, n-1):
        if A[i-1] < A[i] > A[i+1]:
            peaks.append(i)
    def can_place_flags(f):
        """greedy for maximum flexibility in flag placement"""
        if not peaks:
            return False
        placed = 1
        last_placed = peaks[0]
        for i in range(1, len(peaks)):
            if peaks[i] - last_placed >= f:
                last_placed = peaks[i]
                placed += 1
        return placed >= f
    l, r = 0, len(peaks)
    res = 0
    while l <= r:
        m = (l+r) // 2
        if can_place_flags(m):
            res = m
            l = m + 1
        else:
            r = m - 1
    return res