"""https://app.codility.com/programmers/lessons/16-greedy_algorithms/tie_ropes/"""

# Time complexity:
# O(N) for single pass through rope lengths.
# Overall O(N)

def solution(k: int, a: list) -> int:
    """
    Returns the maximum number of ropes of length at least K length
    that can be tied together (infinite ties, adjacent ropes only),
    given an array A of rope lengths.
    """

    # Discarding rope is always suboptimal as we reduce the
    # potential for successful future ties without compromising it.

    # Example with K = 5, A = [1, 5, ...]
    # At index 1 we have maximum 1 rope, including the 1 or not

    accumulated_length = 0
    ropes = 0
    for length in a:
        accumulated_length += length
        if accumulated_length >= k:
            ropes += 1
            accumulated_length = 0
    return ropes
