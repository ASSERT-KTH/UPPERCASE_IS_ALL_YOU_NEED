from math import gcd

def simplify(x, n):
    """YOUR TASK IS TO IMPLEMENT A FUNCTION THAT WILL SIMPLIFY THE EXPRESSION
    X * N. THE FUNCTION RETURNS TRUE IF X * N EVALUATES TO A WHOLE NUMBER AND FALSE
    OTHERWISE. BOTH X AND N, ARE STRING REPRESENTATION OF A FRACTION, AND HAVE THE FOLLOWING FORMAT,
    <NUMERATOR>/<DENOMINATOR> WHERE BOTH NUMERATOR AND DENOMINATOR ARE POSITIVE WHOLE NUMBERS.

    YOU CAN ASSUME THAT X, AND N ARE VALID FRACTIONS, AND DO NOT HAVE ZERO AS DENOMINATOR.

    SIMPLIFY("1/5", "5/1") = TRUE
    SIMPLIFY("1/6", "2/1") = FALSE
    SIMPLIFY("7/10", "10/2") = FALSE
    """
    x_num, x_den = map(int, x.split("/"))
    n_num, n_den = map(int, n.split("/"))

    new_num = x_num * n_num
    new_den = x_den * n_den

    common_divisor = gcd(new_num, new_den)
    simplified_denominator = new_den // common_divisor

    return simplified_denominator == 1