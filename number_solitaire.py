"""https://app.codility.com/programmers/lessons/17-dynamic_programming/number_solitaire/"""

# Time complexity:
# O(N * 6) = O(N), where N is the length of the input

def solution(a: list[int]) -> int:
    """
    Find maximum cumulative score from rolling a six-sided
    die and collecting numbers from the board (start at 0, end at n-1).
    """
    n = len(a)
    dp = [float("-inf")] * n
    dp[0] = a[0]
    # dp[i] is the max score possible at position i
    for i in range(n):
        for j in range(max(i-6, 0), i):

            # Local brute force, we must have rolled any of 1-6 to get to position i,
            # collecting score at i and recording max possible score
            dp[i] = max(dp[i], dp[j] + a[i])

    return dp[n-1]
