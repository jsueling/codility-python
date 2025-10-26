# Time complexity:
# O(N * M) worst case, where N is number of planks and M is number of nails

def solution(A, B, C):
    N, M = len(A), len(C)

    # find the first nail index where we can cumulatively hammer all planks

    hammered = set()
    for nail_i in range(M):
        for plank_i in range(N):
            if A[plank_i] <= C[nail_i] <= B[plank_i]:
                hammered.add(plank_i)
        if len(hammered) == N:
            return nail_i + 1
    return -1

# Time complexity:
# Precomputation sorting is NlogN + MlogM
# Binary search over M nails, which is O(logM) steps
# Each check is O(N + M) in worst case, two finger approach
# Overall O((N + M) logM)

def solution(A, B, C):
    N, M = len(A), len(C)

    # find the first nail index where we can cumulatively hammer all planks

    D = sorted([(A[i], B[i]) for i in range(len(A))])
    E = sorted([(nail_pos, i) for i, nail_pos in enumerate(C)])

    def can_hammer_all_planks(nails):
        i = j = 0
        while True:
            # get next valid nail in sorted order
            while i < M and E[i][1] >= nails:
                i += 1
            if i == M:
                return False
            start, end = D[j]
            nail = E[i][0]
            if nail < start:
                i += 1
            elif nail > end:
                return False
            else:
                j += 1
            if j == N:
                return True

    res = -1
    l, r = 1, M
    while l <= r:
        m = (l+r)//2
        if can_hammer_all_planks(m):
            res = m
            r = m - 1
        else:
            l = m + 1
    return res