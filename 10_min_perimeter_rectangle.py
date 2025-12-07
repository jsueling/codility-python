"""https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/min_perimeter_rectangle/"""

# Time complexity:
# Find factors by checking all numbers up to sqrt(N) with O(1) per check
# Overall: O(sqrt(N))

def solution(n: int) -> int:
    """
    Find min perimeter of rectangle that has area N
    i.e. given N=30
    (1, 30) has perimeter (1+30)*2=62,
    (2,15) has perimeter (2+15)*2=34,
    (3,10) has perimeter (3+10)*2=26,
    (5,6) has perimeter (5+6)*2=22, so return 22
    """

    i = 1
    res = float("inf")
    while i * i <= n:
        q, r = divmod(n, i)
        if r == 0:
            res = min(res, 2 * (i + q))
        i += 1
    return res
