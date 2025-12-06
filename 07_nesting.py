"""https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/"""

# Time complexity:
# Single pass with arithmetic ops and O(1) checks = O(N)
# Overall: O(N)
# Save some space by using counter instead of stack O(N) -> O(1)

def solution(s: str) -> int:
    """
    Return 1 if S is a properly nested string of brackets (same type), else 0.
    ()) is not properly nested
    """

    # Ordering doesn't matter as there is only one bracket type:
    # A closing_bracket can always close the most recently seen opening_bracket,
    # and must to maintain proper nesting.
    open_brackets = 0
    n = len(s)
    for i in range(n):
        if s[i] == '(':
            open_brackets += 1
        else:
            # This logic enforces that as we traverse L-R, each closing
            # bracket can be paired with an open bracket before it
            if open_brackets == 0:
                return 0
            open_brackets -= 1
    return int(open_brackets == 0)
