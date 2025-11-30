"""https://app.codility.com/programmers/lessons/6-sorting/distinct/"""

# Time complexity:
# Put all elements into set is O(N), return its length,
# Overall: O(N)

# Lesson 6 is about sorting, but this approach is more efficient given that
# the array is unsorted. Sort takes O(NlogN) time.

def solution(a: list[int]) -> int:
    """Return number of distinct values in array A."""
    return len(set(a))
