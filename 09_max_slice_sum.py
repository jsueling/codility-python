"""https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/"""

# Time complexity:
# Overall: single pass = O(N)

def solution(a: list[int]) -> int:
    """
    Find max slice sum where the sum of slice (P, Q) (0 <= P <= Q < N)
    is defined as A[P] + A[P+1] + ... + A[Q-1] + A[Q]
    """

    # Kadane's algorithm
    # Let dp[i] be the maximum sum of any slice ending at position i
    # then dp[-1] = 0, meaning the maximum sum of an empty slice is 0.
    # The recurrence relation is then dp[i] = max(0, dp[i-1]) + a[i],
    # meaning either we continue the previous slice or start a new slice at position i.

    max_ending = 0
    max_slice = float("-inf")
    for num in a:
        max_ending = max(0, max_ending) + num
        max_slice = max(max_slice, max_ending)
    return max_slice
