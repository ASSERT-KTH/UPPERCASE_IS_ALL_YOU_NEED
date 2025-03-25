import math

def special_factorial(n):
    """THE BRAZILIAN FACTORIAL IS DEFINED AS:
    BRAZILIAN_FACTORIAL(N) = N! * (N-1)! * (N-2)! * ... * 1!
    WHERE N > 0

    FOR EXAMPLE:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    if n <= 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= math.factorial(i)
    return result