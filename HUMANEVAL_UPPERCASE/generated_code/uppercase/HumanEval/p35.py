def max_element(l: list):
    """RETURN MAXIMUM ELEMENT IN THE LIST.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    maximum = l[0]
    for element in l:
        if element > maximum:
            maximum = element
    return maximum