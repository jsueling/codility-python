"""https://app.codility.com/programmers/lessons/8-leader/dominator/"""

# Time complexity:
# Single pass with simple ops O(N),
# Single frequency count at the end is O(N),
# Overall: O(2N) = O(N)

# Space complexity:
# O(1) with Boyer–Moore majority voting algorithm

# High-level explanation: distinct elements cancel each other out,
# leaving majority element if one exists

def solution(a: list[int]) -> int:
    """Find dominant element in array A"""
    if not a:
        return -1
    candidate_index = -1
    cnt = 0
    n = len(a)
    for i in range(n):
        if cnt == 0:
            candidate_index = i
            cnt = 1
        elif a[i] == a[candidate_index]:
            cnt += 1
        else:
            cnt -= 1
    # If a majority_element exists after exiting the loop it must be a[candidate_index]
    candidate = a[candidate_index]
    # Check if true majority element
    return candidate_index if (a.count(candidate) > n // 2) else -1
