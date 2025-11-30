"""https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/"""

# Time complexity:
# Initialise and precompute 4 prefix sum arrays in O(N),
# Enumerate M queries with O(1) per-query ops in O(M),
# Overall: O(N + M)

def solution(s: str, p: list[int], q: list[int]) -> list[int]:
    """
    A DNA sequence represented as a string consisting of the nucleotides A, C, G and T.
    Each nucleotide has an impact factor: A=1, C=2, G=3, T=4.
    The impact factor of a range of nucleotides is the minimal impact factor of nucleotides
    contained in the DNA sequence between positions P and Q (inclusive).
    E.g. S = CAGCCTA, P = [2,5,0], Q = [4,5,6], range_queries = [[2,5],[5,5],[0,6]] -> result = [2,4,1]
    """

    # My initial idea was range minimum query with segment tree,
    # but we can just enumerate nucleotide types since there are only 4.

    # Precompute prefix sums for each nucleotide type,
    # where prefix_a[i] is the count of nucleotide type A LTE index i in S

    n = len(s)
    prefix_a = [0] * n
    prefix_c = [0] * n
    prefix_g = [0] * n
    prefix_t = [0] * n

    for i in range(n):
        prefix_a[i] = (1 if s[i] == 'A' else 0) + (prefix_a[i - 1] if i-1 >= 0 else 0)
        prefix_c[i] = (1 if s[i] == 'C' else 0) + (prefix_c[i - 1] if i-1 >= 0 else 0)
        prefix_g[i] = (1 if s[i] == 'G' else 0) + (prefix_g[i - 1] if i-1 >= 0 else 0)
        prefix_t[i] = (1 if s[i] == 'T' else 0) + (prefix_t[i - 1] if i-1 >= 0 else 0)

    res = []
    m = len(p)
    for i in range(m):
        start, end = p[i], q[i]
        # Enumerate all possible impact factors, prioritising the smallest
        # Are there any A nucleotide types in S[start:end]?
        if prefix_a[end] - (prefix_a[start-1] if start-1 >= 0 else 0) > 0:
            res.append(1)
        elif prefix_c[end] - (prefix_c[start-1] if start-1 >= 0 else 0) > 0:
            res.append(2)
        elif prefix_g[end] - (prefix_g[start-1] if start-1 >= 0 else 0) > 0:
            res.append(3)
        else:
            res.append(4)
    return res
