"""https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/"""

# Time complexity:
# Single pass with O(1) set op is O(N),
# Overall: O(N)

def solution(x: int, a: list[int]) -> int:
    """
    Frog goal: position 0 to x+1
    Frog can only move on leaves contiguously (no jumps!)
    Leaves settle: time i at position a[i]
    Return earliest time when frog can get from 0 to x+1
    """
    n = len(a)
    positions = set()

    for i in range(n):
        positions.add(a[i])
        if len(positions) == x:
            return i
    return -1
