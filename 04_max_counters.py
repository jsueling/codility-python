"""https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/"""

# Time complexity:
# Init counters array of size N is O(N)
# Single pass through array is O(N), we do O(1) ops per element
# Overall: O(N)

def solution(n: int, a: list[int]) -> list[int]:
    """
    N counters, each initialised to 0
    Each A[i] is an op to do consecutively:
    - increase(X), the Xth counter is increased by 1
    - max_counter where X = N + 1
    After all ops, return value of each counter.
    """
    counters = [0] * n
    max_cnt = 0
    min_cnt = 0
    m = len(a)
    for i in range(m):
        # max_counter op
        if a[i] == n + 1:
            min_cnt = max_cnt
            continue
        # increase(x) op
        if counters[a[i] - 1] < min_cnt:
            counters[a[i] - 1] = min_cnt
        counters[a[i] - 1] += 1
        if counters[a[i] - 1] > max_cnt:
            max_cnt = counters[a[i] - 1]

    return [max(cnt, min_cnt) for cnt in counters]
