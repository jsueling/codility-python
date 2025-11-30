"""https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/"""

# There is a prefix solution but it is slower:
# Let pref(i) be the sum of numbers LTE i divisible by k,
# finally returning pref(b) - pref(a-1).
# Accumulate pref(i) as follows: pref(i) = pref(i-1) + (1 if i % k == 0 else 0)
# We must do this for all i in [0..b], 0 <= a <= b, so time complexity is O(b)

# Time complexity:
# O(1) math ops,
# Overall: O(1)

def solution(a: int, b: int, k: int) -> int:
    """Count integers within range [A..B] that are divisible by K"""
    # Observation: to count multiples of k LTE any number, integer divide by k and add 1
    # E.g. Multiples of 3 LTE 14 are: 0,3,6,9,12 -> 5 = 14//3 + 1
    # So count of multiples of k from a to b (inclusive) is:
    # (b//k + 1) - ((a-1)//k + 1) = b//k - (a-1)//k
    return (b // k) - ((a - 1) // k)
