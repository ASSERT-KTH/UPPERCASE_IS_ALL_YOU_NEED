def sort_third(l: list):
    """THIS FUNCTION TAKES A LIST L AND RETURNS A LIST L' SUCH THAT
    L' IS IDENTICAL TO L IN THE INDICIES THAT ARE NOT DIVISIBLE BY THREE, WHILE ITS VALUES AT THE INDICIES THAT ARE DIVISIBLE BY THREE ARE EQUAL
    TO THE VALUES OF THE CORRESPONDING INDICIES OF L, BUT SORTED.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l_copy = l[:]
    threes = []
    for i in range(len(l)):
        if i % 3 == 0:
            threes.append(l[i])
    threes.sort()
    threes_idx = 0
    for i in range(len(l_copy)):
        if i % 3 == 0:
            l_copy[i] = threes[threes_idx]
            threes_idx += 1

    return l_copy