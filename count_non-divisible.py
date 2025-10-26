from math import sqrt, floor
from collections import Counter

def solution(A):

    count_lookup = Counter(A)
    non_divisible_count = Counter()
    n = len(A)
    for item in count_lookup:
        divisor_count = 0
        for divisor in range(1, floor(sqrt(item)) + 1):
            if (item % divisor == 0):
                complement = item / divisor 
                divisor_count += count_lookup[divisor] 
                if complement != divisor:
                    divisor_count += count_lookup[complement]
                
        num_non_divisor = n - divisor_count
        non_divisible_count[item] = num_non_divisor

    return [non_divisible_count[A[i]] for i in range(n)]