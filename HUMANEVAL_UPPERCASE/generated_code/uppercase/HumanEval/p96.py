def count_up_to(n):
    """IMPLEMENT A FUNCTION THAT TAKES AN NON-NEGATIVE INTEGER AND RETURNS AN ARRAY OF THE FIRST N
    INTEGERS THAT ARE PRIME NUMBERS AND LESS THAN N.
    FOR EXAMPLE:
    COUNT_UP_TO(5) => [2,3]
    COUNT_UP_TO(11) => [2,3,5,7]
    COUNT_UP_TO(0) => []
    COUNT_UP_TO(20) => [2,3,5,7,11,13,17,19]
    COUNT_UP_TO(1) => []
    COUNT_UP_TO(18) => [2,3,5,7,11,13,17]
    """
    if n <= 1:
        return []
    
    primes = []
    num = 2
    while num < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes