"""https://app.codility.com/programmers/lessons/1-iterations/binary_gap/"""

# Time complexity:
# Iterate over the binary representation of n once
# which has log n bits, Overall O(log n)

def solution(n: int) -> int:
    """Return longest sequence of consecutive zeros in binary representation of n"""

    binary_str = bin(n)[2:]
    max_gap = 0
    last_one_idx = -1
    m = len(binary_str)
    for r in range(m):
        if binary_str[r] == '0':
            continue
        max_gap = max(max_gap, r-last_one_idx-1)
        last_one_idx = r
    return max_gap
