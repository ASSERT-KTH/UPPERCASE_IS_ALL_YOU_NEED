import math

def sum_squares(lst):
    """YOU ARE GIVEN A LIST OF NUMBERS.
    YOU NEED TO RETURN THE SUM OF SQUARED NUMBERS IN THE GIVEN LIST,
    ROUND EACH ELEMENT IN THE LIST TO THE UPPER INT(CEILING) FIRST.
    EXAMPLES:
    FOR LST = [1,2,3] THE OUTPUT SHOULD BE 14
    FOR LST = [1,4,9] THE OUTPUT SHOULD BE 98
    FOR LST = [1,3,5,7] THE OUTPUT SHOULD BE 84
    FOR LST = [1.4,4.2,0] THE OUTPUT SHOULD BE 29
    FOR LST = [-2.4,1,1] THE OUTPUT SHOULD BE 6
    

    """
    sum_of_squares = 0
    for num in lst:
        rounded_num = math.ceil(num)
        sum_of_squares += rounded_num**2
    return sum_of_squares