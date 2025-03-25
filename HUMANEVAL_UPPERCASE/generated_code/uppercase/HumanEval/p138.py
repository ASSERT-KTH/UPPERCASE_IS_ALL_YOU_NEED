def is_equal_to_sum_even(n):
    """EVALUATE WHETHER THE GIVEN NUMBER N CAN BE WRITTEN AS THE SUM OF EXACTLY 4 POSITIVE EVEN NUMBERS
    EXAMPLE
    IS_EQUAL_TO_SUM_EVEN(4) == FALSE
    IS_EQUAL_TO_SUM_EVEN(6) == FALSE
    IS_EQUAL_TO_SUM_EVEN(8) == TRUE
    """
    if n <= 8 or n % 2 != 0:
        return False
    else:
        return True