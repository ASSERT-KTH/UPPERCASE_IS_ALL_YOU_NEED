def sum_to_n(n: int):
    """SUM_TO_N IS A FUNCTION THAT SUMS NUMBERS FROM 1 TO N.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum