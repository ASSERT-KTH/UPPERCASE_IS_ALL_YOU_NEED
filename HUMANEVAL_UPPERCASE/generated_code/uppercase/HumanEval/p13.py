def greatest_common_divisor(a: int, b: int) -> int:
    """ RETURN A GREATEST COMMON DIVISOR OF TWO INTEGERS A AND B
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while(b):
        a, b = b, a % b
    return a