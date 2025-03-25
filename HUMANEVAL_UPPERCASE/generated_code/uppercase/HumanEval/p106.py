def f(n):
    """ IMPLEMENT THE FUNCTION F THAT TAKES N AS A PARAMETER,
    AND RETURNS A LIST OF SIZE N, SUCH THAT THE VALUE OF THE ELEMENT AT INDEX I IS THE FACTORIAL OF I IF I IS EVEN
    OR THE SUM OF NUMBERS FROM 1 TO I OTHERWISE.
    I STARTS FROM 1.
    THE FACTORIAL OF I IS THE MULTIPLICATION OF THE NUMBERS FROM 1 TO I (1 * 2 * ... * I).
    EXAMPLE:
    F(5) == [1, 2, 6, 24, 15]
    """
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j
            result.append(factorial)
        else:
            sum_of_numbers = sum(range(1, i + 1))
            result.append(sum_of_numbers)
    return result