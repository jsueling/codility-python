"""https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/"""

# Time complexity:
# Single pass through array, O(N)
# XOR operation is O(log M) where M is the max value,
# but M <= 1,000,000,000 is effectively constant (fits in 32/64 bits)
# Overall = O(N)

def solution(a: list[int]) -> int:
    """
    Each element of array A appears an even number of times,
    except for one element which appears an odd number of times.
    Return that odd occurring element.
    """
    result = 0
    # XOR is commutative, associative and self-inverse.
    # All pairs cancel, leaving the odd occurring number
    for number in a:
        result ^= number
    return result
