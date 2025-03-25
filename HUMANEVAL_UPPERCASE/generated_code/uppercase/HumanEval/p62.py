def derivative(xs: list):
    """ XS REPRESENT COEFFICIENTS OF A POLYNOMIAL.
    XS[0] + XS[1] * X + XS[2] * X^2 + ....
     RETURN DERIVATIVE OF THIS POLYNOMIAL IN THE SAME FORM.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    derivative_coefficients = []
    for i in range(1, len(xs)):
        derivative_coefficients.append(xs[i] * i)
    return derivative_coefficients