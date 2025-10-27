"""https://app.codility.com/programmers/lessons/16-greedy_algorithms/max_nonoverlapping_segments/"""

# Time complexity:
# O(N) for single pass through segments, input is pre-sorted by ends.
# Overall O(n)

def solution(a: list, b: list) -> int:
    """
    Find the maximum number of non-overlapping segments
    where a[i] is the start and b[i] is the end of segment i.
    """
    n = len(a)
    res = 0
    last_end = -1
    for i in range(n):
        s, e = a[i], b[i]
        # If no overlap, increment count + update last_end
        if last_end < s:
            res += 1
            last_end = b[i]
        else: # Overlap, pick the earliest ending segment to maximise space for future segments
            last_end = min(last_end, e)
    return res
