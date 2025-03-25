def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
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
    result = 1
    power_of_2 = 2
    n = n % (p - 1)
    for _ in range(n):
        result = (result * power_of_2) % p
    return result