import math

def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    try:
        num = float(value)
    except ValueError:
        return None
    
    if num == int(num):
        return int(num)

    lower = math.floor(num)
    upper = math.ceil(num)

    if abs(num - lower) < abs(num - upper):
        return int(lower)
    elif abs(num - lower) > abs(num - upper):
        return int(upper)
    else: # equidistant. round away from zero
        if num > 0:
            return int(upper)
        else:
            return int(lower)