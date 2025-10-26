# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    n = len(A)
    A.append(1)
    def fib(n):
        nums = [0, 1]
        while nums[-1] < n + 2:
            nums.append(nums[-1] + nums[-2])
        return nums[2:]
    nums = fib(n)
    dp = [float("inf")] * (n+1)
    for i in range(len(dp)):
        if A[i] == 0:
            continue
        for j in range(len(nums)):
            hop = i-nums[j]
            if hop < -1:
                continue
            elif hop == -1:
                dp[i] = 1
            elif A[hop] == 1:
                dp[i] = min(dp[i], 1 + dp[hop])
    return -1 if dp[n] == float("inf") else dp[n]