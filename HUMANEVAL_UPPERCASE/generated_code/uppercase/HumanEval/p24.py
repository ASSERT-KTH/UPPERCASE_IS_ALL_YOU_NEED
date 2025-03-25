def largest_divisor(n: int) -> int:
    """ FOR A GIVEN NUMBER N, FIND THE LARGEST NUMBER THAT DIVIDES N EVENLY, SMALLER THAN N
    >>> largest_divisor(15)
    5
    """
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i