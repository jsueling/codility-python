"""https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/"""

# Time complexity:
# Sorting is O(NlogN), checking 2 cases is O(1),
# Overall: O(NlogN)

def solution(a: list[int]) -> int:
    """Find max product of any triplet in array A"""
    a.sort()
    # Greedily consider only 2 cases:
    return max(
        # 1. Top 3 largest (all positive, or least negative)
        a[-1] * a[-2] * a[-3],
        # 2. If 2 smallest are negative, we pair them with the largest (positive, or least negative)
        a[0] * a[1] * a[-1],
    )
