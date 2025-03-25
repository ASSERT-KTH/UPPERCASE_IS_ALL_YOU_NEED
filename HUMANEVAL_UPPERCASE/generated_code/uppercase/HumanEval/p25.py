from typing import List


def factorize(n: int) -> List[int]:
    """ RETURN LIST OF PRIME FACTORS OF GIVEN INTEGER IN THE ORDER FROM SMALLEST TO LARGEST.
    EACH OF THE FACTORS SHOULD BE LISTED NUMBER OF TIMES CORRESPONDING TO HOW MANY TIMES IT APPEARES IN FACTORIZATION.
    INPUT NUMBER SHOULD BE EQUAL TO THE PRODUCT OF ALL FACTORS
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors