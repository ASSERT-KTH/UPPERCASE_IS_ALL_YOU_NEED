def common(l1: list, l2: list):
    """RETURN SORTED UNIQUE COMMON ELEMENTS FOR TWO LISTS.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    s1 = set(l1)
    s2 = set(l2)
    common_elements = sorted(list(s1.intersection(s2)))
    return common_elements