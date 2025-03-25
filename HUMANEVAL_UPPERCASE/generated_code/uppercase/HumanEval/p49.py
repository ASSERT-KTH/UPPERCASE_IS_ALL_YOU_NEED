def modp(n: int, p: int):
    """RETURN 2^N MODULO P (BE AWARE OF NUMERICS).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    result = pow(2, n, p)
    return result