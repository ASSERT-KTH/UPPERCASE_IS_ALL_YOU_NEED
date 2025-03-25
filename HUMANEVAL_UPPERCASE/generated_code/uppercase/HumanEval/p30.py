def get_positive(l: list):
    """RETURN ONLY POSITIVE NUMBERS IN THE LIST.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    positive_numbers = [num for num in l if num > 0]
    return positive_numbers