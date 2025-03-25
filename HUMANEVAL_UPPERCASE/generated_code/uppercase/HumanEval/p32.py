import math


def poly(xs: list, x: float):
    """
    EVALUATES POLYNOMIAL WITH COEFFICIENTS XS AT POINT X.
    RETURN XS[0] + XS[1] * X + XS[1] * X^2 + .... XS[N] * X^N
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ XS ARE COEFFICIENTS OF A POLYNOMIAL.
    FIND_ZERO FIND X SUCH THAT POLY(X) = 0.
    FIND_ZERO RETURNS ONLY ONLY ZERO POINT, EVEN IF THERE ARE MANY.
    MOREOVER, FIND_ZERO ONLY TAKES LIST XS HAVING EVEN NUMBER OF COEFFICIENTS
    AND LARGEST NON ZERO COEFFICIENT AS IT GUARANTEES
    A SOLUTION.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2 != 0:
        raise ValueError("Input list must have an even number of coefficients.")

    # Use the bisection method to find a root.
    # Find a range where the function changes sign.
    a = -100  # Start with a large negative value
    b = 100   # and a large positive one
    if poly(xs, a) * poly(xs, b) > 0:  # If no sign change use smarter range finder
        a =- 10
        b = 10
        for i in range(1,1000):
            if poly(xs,a) * poly(xs,b) < 0:
                break
            a-=10
            b+=10
        if poly(xs,a) * poly(xs,b) > 0:
            raise ValueError("No root found within reasonable bounds. Consider expanding the search range.")


    # Bisection method
    for _ in range(100):  # Iterate a sufficient number of times for accuracy
        c = (a + b) / 2
        if poly(xs, c) == 0:
            return c
        if poly(xs, a) * poly(xs, c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2  # Return the approximate root