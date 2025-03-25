def truncate_number(number: float) -> float:
    """ GIVEN A POSITIVE FLOATING POINT NUMBER, IT CAN BE DECOMPOSED INTO
    AND INTEGER PART (LARGEST INTEGER SMALLER THAN GIVEN NUMBER) AND DECIMALS
    (LEFTOVER PART ALWAYS SMALLER THAN 1).

    RETURN THE DECIMAL PART OF THE NUMBER.
    >>> truncate_number(3.5)
    0.5
    """

    integer_part = int(number)
    decimal_part = number - integer_part

    return decimal_part