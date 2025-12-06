"""https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/"""

# Time complexity:
# Single pass with push/pop/check is O(N) with O(1) work per element,
# Overall: O(N)

def solution(s: str) -> int:
    """
    Return 1 if S is a properly nested string of brackets (diff types), else 0.
    {[}] is not properly nested
    """
    stack = []
    n = len(s)
    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for i in range(n):
        if s[i] in bracket_map:
            # closing_bracket must match most recent open_bracket or not properly nested
            if not stack or stack[-1] != bracket_map[s[i]]:
                return 0
            stack.pop()
        else:
            stack.append(s[i])

    return 1 if not stack else 0
