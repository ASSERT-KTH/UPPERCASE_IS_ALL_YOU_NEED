def median(l: list):
    """RETURN MEDIAN OF ELEMENTS IN THE LIST L.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    l_sorted = sorted(l)
    if n % 2 == 1:
        return l_sorted[n // 2]
    else:
        return (l_sorted[n // 2 - 1] + l_sorted[n // 2]) / 2