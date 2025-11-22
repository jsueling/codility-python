"""https://app.codility.com/programmers/lessons/14-binary_search_algorithm/nailing_planks/"""

# Time complexity:
# O(N * M) worst case, where N is number of planks and M is number of nails
# Correct but fails performance tests:
# ▶ random_medium
# random sequence, length = ~10,000 ✘TIMEOUT ERROR
# running time: 4.904 sec., time limit: 0.262 sec.
# ▶ random_large
# random sequence, length = ~30,000 ✘TIMEOUT ERROR
# Killed. Hard limit reached: 6.000 sec.
# ▶ extreme_large_planks
# all large planks, length = ~30,000 ✘TIMEOUT ERROR
# Killed. Hard limit reached: 6.000 sec.
# ▶ large_point
# all planks are points, length = ~30,000 ✘TIMEOUT ERROR
# Killed. Hard limit reached: 6.000 sec.

def solution_a(a: list, b: list, c: list) -> int:
    """
    Array A and B of N planks (start and end positions inclusive). (A[i] <= B[i])
    Array C of M nails (positions).
    Find the first nail index where we can cumulatively hammer all planks
    """
    n, m = len(a), len(c)

    hammered = set()
    for nail_i in range(m):
        for plank_i in range(n):
            if a[plank_i] <= c[nail_i] <= b[plank_i]:
                hammered.add(plank_i)
        if len(hammered) == n:
            return nail_i + 1
    return -1

# Optimised time complexity:
# Precomputation sorting is NlogN + MlogM
# Binary search over (r-l) = M nails, which is O(logM) steps
# Each check is O(N + M) in worst case, two finger approach
# Overall = O((N + M) * logM + NlogN + MlogM) = O((N + M) * logM + NlogN)

def solution_b(a: list, b: list, c: list) -> int:
    """Binary search over nails to find first nail index to hammer all planks"""
    plank_count, nail_count = len(a), len(c)

    plank_ranges = sorted([(a[i], b[i]) for i in range(len(a))])
    sorted_nail_positions = sorted([(nail_pos, i) for i, nail_pos in enumerate(c)])

    def can_hammer_all_planks(available_nails):
        nail_index = plank_index = 0
        while True:
            # Get the earliest available nail, skipping nails not available
            while nail_index < nail_count and sorted_nail_positions[nail_index][1] >= available_nails:
                nail_index += 1
            if nail_index == nail_count: # No more nails to try
                return False

            # Current plank to hammer and nail to try
            start, end = plank_ranges[plank_index]
            nail = sorted_nail_positions[nail_index][0]

            if nail < start: # Try the next nail
                nail_index += 1
            elif nail > end: # This plank cannot be hammered, fail
                return False
            else: # This plank is hammered, go to next plank
                plank_index += 1

            if plank_index == plank_count: # All planks hammered
                return True

    res = -1
    l, r = 1, nail_count
    while l <= r:
        m = (l+r)//2
        # Find lowest m, number of nails, where we can hammer all planks
        if can_hammer_all_planks(m):
            res = m
            r = m - 1
        else:
            l = m + 1
    return res
