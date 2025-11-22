"""https://app.codility.com/programmers/lessons/15-caterpillar_method/abs_distinct/"""

# Time complexity:
# There is a two pointer approach as the array is sorted,
# but it's not better than O(N) using a set so overall O(N)

def solution(a: list) -> int:
    """
    Count number of distinct absolute values in array
    """
    return len({ abs(x) for x in a })
