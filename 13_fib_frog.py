"""https://app.codility.com/programmers/lessons/13-fibonacci_numbers/fib_frog/"""

# Time complexity:
# Generate Fibonacci numbers until no larger than N: O(log N)
# DP to find min jumps: O(N * M) where M is number of generated Fibonacci numbers
# Overall: O(N log N)

def solution(a: list) -> int:
    """
    Find min frog jumps to cross river.
    Frog can jump distances equal to any Fibonacci number.
    """
    n = len(a)
    a.append(1) # add landing bank

    def fib(n):
        """Generates Fibonacci numbers LTE n+1 (Largest jump is -1 -> landing-bank)"""
        nums = [0, 1]
        while nums[-1] <= n+1:
            nums.append(nums[-1] + nums[-2])
        return nums

    jump_distances = fib(n)
    dp = [float("inf")] * (n+1)

    for i in range(n+1):
        if a[i] == 0:
            continue

        for jump in jump_distances:
            prev_pos = i - jump
            if prev_pos < -1:
                continue
            if prev_pos == -1:
                dp[i] = 1
            # local brute force, jump from prev_pos to i
            elif a[prev_pos] == 1:
                dp[i] = min(dp[i], 1 + dp[prev_pos])

    return -1 if dp[n] == float("inf") else dp[n]
