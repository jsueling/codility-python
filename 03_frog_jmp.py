"""https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/"""

# Time complexity:
# Only math ops, overall: O(1)

from math import ceil

def solution(x: int, y: int, d: int) -> int:
    """
    Return min jumps from position x to y or greater with jump distance d
    """
    # As jumps are discrete, we round up the result of dividing dist_to_cover by jump distance, d
    dist_to_cover = y - x
    return ceil(dist_to_cover / d)
