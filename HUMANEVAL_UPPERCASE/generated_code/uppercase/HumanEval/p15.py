def string_sequence(n: int) -> str:
    """ RETURN A STRING CONTAINING SPACE-DELIMITED NUMBERS STARTING FROM 0 UPTO N INCLUSIVE.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ' '.join(map(str, range(n + 1)))