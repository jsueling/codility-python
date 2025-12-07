"""https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/peaks/"""

# Time complexity:
# Precomputing factors (candidate block sizes) = O(sqrt(N))
# Precomputing peaks = O(N)
# Iterating over all factors worst case O(sqrt(N))
# Each factor check is O(N) from scanning through all peaks.
# Overall: O(N + sqrt(N) * N) = O(N*sqrt(N))

def solution_a(a: list[int]) -> int:
    """
    Split array A into max number of blocks where:
    1. Each block contains the same number of elements
    2. Each block contains at least one peak
    
    My solution passes 100%, Codility detects O(N * log(log(N))) time complexity
    """

    n = len(a)

    factors = []
    i = 1
    while i * i <= n:
        q, r = divmod(n, i)
        if r == 0:
            if q != i:
                factors.extend([i, q])
            else:
                factors.append(i) # Perfect square
        i += 1
    factors.sort()

    peaks = []
    for i in range(1, n-1):
        if a[i-1] < a[i] > a[i+1]:
            peaks.append(i)

    def can_div(index):
        """Can we divide A into factors[index] blocks with at least one peak each?"""
        num_blocks = factors[index]
        block_end = 0
        peak_index = 0
        block_size = n // num_blocks
        while True:
            block_end += block_size
            last_peak_index = peak_index
            # Find peaks in current block
            while peak_index < len(peaks) and peaks[peak_index] < block_end:
                peak_index += 1
            # At least one peak must exist in the current block,
            # we may have exhausted all peaks
            if last_peak_index == peak_index:
                return num_blocks == 0
            num_blocks -= 1

    # Initially tried binary search on factors but can_div is not monotonic,
    # so fails on some cases. Instead just go largest to smallest.

    # To see why consider array of length 12 with peaks at indices (2, 3, 8, 9)
    # 3 blocks of size 4 can_div FAILS
    # 0 0 1 1 | 0 0 0 0 | 1 1 0 0
    # 4 blocks of size 3 can_div SUCCEEDS
    # 0 0 1 | 1 0 0 | 0 0 1 | 1 0 0
    # In this example, if binary search tried 3 blocks first, it would miss the solution,
    # since 4 blocks is possible.

    for i in range(len(factors)-1,-1,-1):
        if can_div(i):
            return factors[i]
    return 0

# Time complexity:
# Precompute prefix peaks array = O(N)
# Precompute factors = O(sqrt(N))
# Sort factors = O(sqrt(N) * log(sqrt(N)))
# Outer loop runs for each factor (at most 2 * sqrt(N) iterations)
# Inner loop does total work O(N log log N) across all iterations (sum of factors of N)
# Overall: O(N + 3 * sqrt(N) + sqrt(N) * log(sqrt(N)) + N log log N) = O(N log log N)

def solution_b(a: list[int]) -> int:
    """
    Optimised solution_a with help from gemini-3-pro (explanations added)
    Codility detects O(N * log(log(N))) time complexity
    """
    n = len(a)

    # peaks_count[i] stores the number of peaks in a[0...i-1] (Exclusive of i)
    peaks_count = [0] * (n + 1)
    for i in range(1, n - 1):
        peaks_count[i+1] = peaks_count[i]
        if a[i-1] < a[i] > a[i+1]:
            peaks_count[i+1] += 1
    peaks_count[n] = peaks_count[n-1]

    if peaks_count[n] == 0:
        return 0

    factors = []
    i = 1
    while i * i <= n:
        q, r = divmod(n, i)
        if r == 0:
            if q != i:
                factors.extend([i, q])
            else:
                factors.append(i) # Perfect square
        i += 1
    factors.sort(reverse=True)

    # Outer loop: 2 * sqrt(N) maximum number of factors of N
    for num_blocks in factors:
        block_size = n // num_blocks
        valid = True
        # Inner loop: Over all factors of N, this loop runs in O(N log log N) time total
        # as each factor F does at most F work (num_blocks = F),
        # and the sum of all factors of N is N log log N
        for i in range(num_blocks):
            start_idx = i * block_size
            end_idx = (i + 1) * block_size
            # O(1) prefix sum check, every block has at least one peak
            if peaks_count[end_idx] - peaks_count[start_idx] == 0:
                valid = False
                break
        if valid is True:
            return num_blocks
    return 0
