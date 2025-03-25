import math

def is_simple_power(x, n):
    """YOUR TASK IS TO WRITE A FUNCTION THAT RETURNS TRUE IF A NUMBER X IS A SIMPLE
    POWER OF N AND FALSE IN OTHER CASES.
    X IS A SIMPLE POWER OF N IF N**INT=X
    FOR EXAMPLE:
    IS_SIMPLE_POWER(1, 4) => TRUE
    IS_SIMPLE_POWER(2, 2) => TRUE
    IS_SIMPLE_POWER(8, 2) => TRUE
    IS_SIMPLE_POWER(3, 2) => FALSE
    IS_SIMPLE_POWER(3, 1) => FALSE
    IS_SIMPLE_POWER(5, 3) => FALSE
    """
    if n <= 1:
        return x == 1 or (n == 1 and x == 1 )
    if x <= 0:
        return x == 0
    if x == 1:
        return True

    power = round(math.log(x, n))
    return n ** power == x