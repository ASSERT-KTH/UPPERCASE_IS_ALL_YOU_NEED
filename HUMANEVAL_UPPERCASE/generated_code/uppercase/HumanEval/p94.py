def skjkasdkd(lst):
    """YOU ARE GIVEN A LIST OF INTEGERS.
    YOU NEED TO FIND THE LARGEST PRIME VALUE AND RETURN THE SUM OF ITS DIGITS.

    EXAMPLES:
    FOR LST = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] THE OUTPUT SHOULD BE 10
    FOR LST = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] THE OUTPUT SHOULD BE 25
    FOR LST = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] THE OUTPUT SHOULD BE 13
    FOR LST = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] THE OUTPUT SHOULD BE 11
    FOR LST = [0,81,12,3,1,21] THE OUTPUT SHOULD BE 3
    FOR LST = [0,8,1,2,1,7] THE OUTPUT SHOULD BE 7
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    largest_prime = -1
    for num in lst:
        if is_prime(num):
            largest_prime = max(largest_prime, num)

    if largest_prime == -1:
        return 0

    sum_of_digits = sum(int(digit) for digit in str(largest_prime))
    return sum_of_digits