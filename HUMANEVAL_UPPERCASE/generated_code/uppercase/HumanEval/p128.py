def prod_signs(arr):
    """
    YOU ARE GIVEN AN ARRAY ARR OF INTEGERS AND YOU NEED TO RETURN
    SUM OF MAGNITUDES OF INTEGERS MULTIPLIED BY PRODUCT OF ALL SIGNS
    OF EACH NUMBER IN THE ARRAY, REPRESENTED BY 1, -1 OR 0.
    NOTE: RETURN NONE FOR EMPTY ARR.

    EXAMPLE:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if not arr:
        return None

    sign_product = 1
    for num in arr:
        if num > 0:
            sign_product *= 1
        elif num < 0:
            sign_product *= -1
        else:
            sign_product = 0
            break

    sum_magnitudes = sum(abs(num) for num in arr)

    return sign_product * sum_magnitudes