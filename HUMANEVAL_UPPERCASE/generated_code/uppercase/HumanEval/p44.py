def change_base(x: int, base: int):
    """CHANGE NUMERICAL BASE OF INPUT NUMBER X TO BASE.
    RETURN STRING REPRESENTATION AFTER THE CONVERSION.
    BASE NUMBERS ARE LESS THAN 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    digits = []
    while x:
        digits.append(str(x % base))
        x //= base
    return ''.join(digits[::-1])