"""https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/"""

# Time complexity:
# Single pass, Overall = O(N)

def solution(a: list[int]) -> int:
    """
    Find maximum profit given stock prices in array A,
    where buy price is P and sell price is Q and 0 <= P <= Q < N
    """
    max_profit = 0
    buy = float("inf")
    for price in a:
        # Buy and sell actions are single events (no slice)
        max_profit = max(max_profit, price - buy)
        # We always improve profit by buying lower (must be before sell)
        buy = min(buy, price)
    return max_profit
