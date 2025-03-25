def x_or_y(n, x, y):
    """A SIMPLE PROGRAM WHICH SHOULD RETURN THE VALUE OF X IF N IS 
    A PRIME NUMBER AND SHOULD RETURN THE VALUE OF Y OTHERWISE.

    EXAMPLES:
    FOR X_OR_Y(7, 34, 12) == 34
    FOR X_OR_Y(15, 8, 5) == 5
    
    """
    if n <= 1:
        return y  # Numbers less than or equal to 1 are not prime
    if n <= 3:
        return x  # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return y  # Check divisibility by 2 and 3
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return y  # Check divisibility by numbers of the form 6k +/- 1
        i += 6
    return x  # If no divisors found, 'n' is prime