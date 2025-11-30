"""https://app.codility.com/programmers/lessons/6-sorting/triangle/"""

# Time complexity:
# Sorting is O(NlogN), single pass with triplet checking is O(N),
# Overall: O(NlogN)

def solution(a: list[int]) -> int:
    """
    Array A contains lengths of lines that can form triangles.
    Valid triangles can only be formed if the sum of any two sides is GT the third side.
    Return 1 if possible to form a triangle with any 3 lines, else 0.
    """
    n = len(a)
    a.sort()
    # We observe that a valid triplet must have a longest side present in the array.
    # Let S1 be the longest side in the array. If we consider each element in the array as S1,
    # then there are 3 triangle conditions for S1, S2 and S3:
    #   1. S1 + S2 > S3
    #   2. S1 + S3 > S2
    #   3. S2 + S3 > S1
    # Conditions 1 and 2 always hold since S1 is the longest side, S1 >= S3 and S1 >= S2
    # Greedily, if condition 3 can be satisfied by any other sides (S2, S3), the sides immediately 
    # preceding the longest side in sorted order will satisfy condition 3
    return 1 if any((a[i] > 0 and a[i] + a[i+1] > a[i+2]) for i in range(n-2)) else 0

    # "each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].""

    # Note on non-positive lengths:
    #   If A[i] <= 0, 
    #   A[i+1] <= A[i+2], always since sorted order
    #   then A[i] + A[i+1] <= A[i+2], the condition A[i] + A[i+1] > A[i+2] fails
