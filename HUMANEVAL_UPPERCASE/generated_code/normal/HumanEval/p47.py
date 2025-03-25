def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    list_len = len(sorted_l)

    if list_len % 2 == 0:
        # Even length: median is the average of the two middle elements
        mid1 = sorted_l[list_len // 2 - 1]
        mid2 = sorted_l[list_len // 2]
        median_val = (mid1 + mid2) / 2.0
    else:
        # Odd length: median is the middle element
        median_val = sorted_l[list_len // 2]
    return median_val