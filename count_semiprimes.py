# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from math import floor, sqrt
def solution(N, P, Q):
    # Implement your solution here
    
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False
    i = 2

    while i * i <= N:
        if sieve[i]:
            k = i * i
            while k <= N:
                sieve[k] = False
                k += i
        i += 1
    
    cur = 0
    prefix = [0]
    for i in range(1, N+1):
        for j in range(1, floor(sqrt(i)) + 1):
            if sieve[j] and i % j == 0 and sieve[i // j]:
                cur += 1
        prefix.append(cur)
    return [prefix[Q[i]]-prefix[P[i]-1] for i in range(len(P))]