def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    n = len(s)
    shift = shift % n  # Handle shifts larger than the number of digits
    if shift == 0:
        return s
    shifted_s = s[-shift:] + s[:-shift]
    return shifted_s