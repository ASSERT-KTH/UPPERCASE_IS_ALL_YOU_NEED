import math

def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if n <= 1:
        return x == 1 or (n == 1 and x == 1)
    if x <= 0:
        return x == 0
    if x == 1:
        return True
    
    power =  math.log(x, n)
    return abs(power - round(power)) < 1e-9 # Check if the power is an integer