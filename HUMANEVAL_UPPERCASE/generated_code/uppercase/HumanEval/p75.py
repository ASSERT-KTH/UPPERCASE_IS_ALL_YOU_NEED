def is_multiply_prime(a):
    """WRITE A FUNCTION THAT RETURNS TRUE IF THE GIVEN NUMBER IS THE MULTIPLICATION OF 3 PRIME NUMBERS
    AND FALSE OTHERWISE.
    KNOWING THAT (A) IS LESS THEN 100. 
    EXAMPLE:
    IS_MULTIPLY_PRIME(30) == TRUE
    30 = 2 * 3 * 5
    """
    if a < 2:
        return False
    
    primes = []
    
    # Find prime factors
    d = 2
    temp = a
    while d * d <= temp:
        if temp % d == 0:
            primes.append(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        primes.append(temp)
        
    if len(primes) != 3:
        return False
    
    # Check if factors are prime
    for p in primes:
      if p < 2:
          return False
      for i in range(2, int(p**0.5) + 1):
          if p % i == 0:
              return False
    
    return True