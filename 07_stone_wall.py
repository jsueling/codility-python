"""https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/"""

# Time complexity:
# Overall: O(N) single pass through array with O(1) stack ops per item

def solution(h: list[int]) -> int:
    """
    Given array H representing heights of wall segments,
    return minimum number of blocks needed to build the wall.
    Each block can be any height, but must be rectangular.
    """
    stack = []
    n = len(h)
    blocks = 0
    for i in range(n):

        # While traversing L-R, maintain monotonic increasing stack representing
        # existing blocks that possibly could be reused (extended to the right)

        # 1. Finding a taller block than most recent requires a new block
        # 2. Finding shorter block makes it impossible to reuse taller existing blocks
        #    (stack invalidation) i.e. rightwards extension impossible
        # 3. After validating the stack, if block height is the same as the most recent
        #    existing block we reuse and do not add an additional block 

        while stack and stack[-1] > h[i]:
            stack.pop()
        if not stack or stack[-1] < h[i]:
            stack.append(h[i])
            blocks += 1
    return blocks
