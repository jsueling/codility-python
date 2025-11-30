"""https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/"""

# Time complexity:
# Building and sorting start and ending disc boundaries is worst case 2 * (N + NlogN),
# Iterating over disc boundaries is O(N),
# Overall: O(2 * NlogN + 3 * N) = O(NlogN)

def solution(a: list[int]) -> int:
    """Return number of intersecting discs drawn on a plane."""

    n = len(a)
    starts, ends = {}, {} # beginning and end points of all discs boundaries
    for i in range(n):
        s, e = i-a[i], i+a[i]+1 # end is exclusive
        starts[s] = starts.get(s, 0) + 1
        ends[e] = ends.get(e, 0) - 1

    # We draw N discs on a plane. The discs are numbered from 0 to N - 1.
    # An array A of N non-negative integers, specifying the radii of the discs, is given.
    # The J-th disc is drawn with its center at (J, 0) and radius A[J].

    # N is an integer within the range [0..100,000];
    # each element of array A is an integer within the range [0..2,147,483,647].

    # Enumerating sorted disc_boundaries:
    #   Sort NlogN start_boundaries and end_boundaries is at worst 2 * 100_000log100_000 = 1,000,000 ops
    #   Iterating over sorted boundaries with pointers is at worst 100,000 ops
    # Enumerating all possible disc boundary indices:
    #   [0 - 2,147,483,647, 100,000 + 2,147,483,647] = ~4e9 ops

    sorted_start_keys = sorted(starts)
    sorted_end_keys = sorted(ends)

    start_pointer = end_pointer = 0
    intersecting = 0
    active_discs = 0
    # Impossible to go out of bounds on end pointers,
    # since each and every start has a corresponding end (and end > start)
    while start_pointer < len(sorted_start_keys):
        s1 = sorted_start_keys[start_pointer]
        e1 = sorted_end_keys[end_pointer]
        # Deactivate discs if end boundary is before or at current start boundary
        if e1 <= s1:
            active_discs += ends[e1]
            end_pointer += 1
        # Count new intersections if start boundary is before or at current end boundary
        # (Discs are deactivated first if s1 == e1 as end_boundaries are exclusive)
        if s1 <= e1:
            incoming = starts[s1]
            # Each incoming disc pairs (intersects) with every other incoming disc and all currently active discs.
            # E.g. 4 active, 3 incoming
            # 1st incoming pairs with 6 (4 active + 2nd and 3rd incoming)
            # 2nd incoming pairs with 5 (4 active + 3rd incoming)
            # 3rd incoming pairs with 4 active
            # = 6 + 5 + 4
            # Sum of arithmetic series = n * (a_1 + a_n) // 2,
            # where a_1 and a_n are first and last terms
            intersecting += (incoming * (active_discs + (active_discs + incoming - 1))) // 2
            if intersecting > 10_000_000:
                return -1
            active_discs += incoming
            start_pointer += 1
    return intersecting
