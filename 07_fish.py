"""https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/"""

# Time complexity:
# Overall: O(N) single pass with O(1) stack ops

def solution(a: list[int], b: list[int]) -> int:
    """
    Array A and B represent voracious fish in a river.
    Upstream fish are at lower indices, downstream fish are at higher indices.
    Index i in A and B represent the size and direction of fish i.
    B[i] = 0/1 represents a fish going to lower indices/higher indices respectively
    """
    stack = []
    n = len(a)
    alive = n
    for i in range(n-1,-1,-1):
        if b[i] == 0:
            stack.append(i)
        else:
            while stack:
                # "the elements of A are all distinct" guarantees a fish always eats the other
                alive -= 1
                if a[stack[-1]] > a[i]:
                    break
                stack.pop()
            # Fish going downstream either is eaten or encounters no more fish going upstream
    return alive
