"""https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/"""

# Time complexity:
# Precompute Max slice ending at and max slice starting at arrays = O(N)
# Iterate over array, fixing Y and storing max double slice seen for each = O(N)
# Overall: O(2N) = O(N)

def solution(a: list[int]) -> int:
    """
    The sum of a double slice is (X, Y, Z) is defined as
    A[X + 1] + A[X + 2] + ... + A[Y - 1] + A[Y + 1] + A[Y + 2] + ... + A[Z - 1]
    where 0 ≤ X < Y < Z < N. Note: A[X], A[Y] and A[Z] are excluded from this sum
    Find max double slice sum in array A.
    """

    # Variations of Kadane's algorithm:
    # 1. Empty subarrays are disallowed, must include at least this element
    #    dp[i] = max(0, dp[i-1]) + a[i]
    # 2. Empty subarrays are allowed e.g. X[]Y[1,2,3]Z
    #    dp[i] = max(0, dp[i-1] + a[i])

    n = len(a)
    max_slice_ending_at = [0] * n
    max_slice_starting_at = [0] * n
    for i in range(1, n-1):
        max_slice_ending_at[i] = max(0, max_slice_ending_at[i-1] + a[i])
        max_slice_starting_at[n-i-1] = max(0, max_slice_starting_at[n-i] + a[n-i-1])
    return max(max_slice_ending_at[i-1] + max_slice_starting_at[i+1] for i in range(1, n-1))
