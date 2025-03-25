def digits(n):
    """GIVEN A POSITIVE INTEGER N, RETURN THE PRODUCT OF THE ODD DIGITS.
    RETURN 0 IF ALL DIGITS ARE EVEN.
    FOR EXAMPLE:
    DIGITS(1)  == 1
    DIGITS(4)  == 0
    DIGITS(235) == 15
    """
    product = 1
    has_odd = False
    for digit in str(n):
        digit = int(digit)
        if digit % 2 != 0:
            product *= digit
            has_odd = True
    if not has_odd:
        return 0
    return product