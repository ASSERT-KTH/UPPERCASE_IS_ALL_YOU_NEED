def fizz_buzz(n: int):
    """RETURN THE NUMBER OF TIMES THE DIGIT 7 APPEARS IN INTEGERS LESS THAN N WHICH ARE DIVISIBLE BY 11 OR 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            s = str(i)
            count += s.count('7')
    return count