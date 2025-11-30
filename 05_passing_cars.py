"""https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/"""

# Time complexity:
# Precompute suffix sum in O(N),
# Single pass O(N) with O(1) per-element ops: update to suffix sum or count passing cars,
# Overall: O(N)

def solution(a: list[int]) -> int:
    """
    Count passing cars on the road.
    Each element in A is either: 0 car going east, 1 car going west
    For P, Q in range [0, N-1], if P < Q, A[P] = 0 and A[Q] = 1,
    then car P will pass car Q.
    E.g. A = [0,1,0,1,1] -> 5 passing cars
    Return number of passing cars or -1 if exceeds 1,000,000,000
    """
    n = len(a)
    west = sum(a) # suffix sum
    passing_cars = 0
    for i in range(n):
        if a[i] == 0:
            passing_cars += west
            if passing_cars > 1_000_000_000:
                return -1
        else:
            west -= 1
    return passing_cars
