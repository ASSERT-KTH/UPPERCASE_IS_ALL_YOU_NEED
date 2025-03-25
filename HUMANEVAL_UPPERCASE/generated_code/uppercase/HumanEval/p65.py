def circular_shift(x, shift):
    """CIRCULAR SHIFT THE DIGITS OF THE INTEGER X, SHIFT THE DIGITS RIGHT BY SHIFT
    AND RETURN THE RESULT AS A STRING.
    IF SHIFT > NUMBER OF DIGITS, RETURN DIGITS REVERSED.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    n = len(s)

    if shift > n:
        return s[::-1]

    shift = shift % n

    shifted_s = s[-shift:] + s[:-shift]
    return shifted_s