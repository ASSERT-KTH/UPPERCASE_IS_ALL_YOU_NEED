def largest_prime_factor(n: int):
    """RETURN THE LARGEST PRIME FACTOR OF N. ASSUME N > 1 AND IS NOT A PRIME.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n