def generate_integers(a, b):
    """
    GIVEN TWO POSITIVE INTEGERS A AND B, RETURN THE EVEN DIGITS BETWEEN A
    AND B, IN ASCENDING ORDER.

    FOR EXAMPLE:
    GENERATE_INTEGERS(2, 8) => [2, 4, 6, 8]
    GENERATE_INTEGERS(8, 2) => [2, 4, 6, 8]
    GENERATE_INTEGERS(10, 14) => []
    """
    even_digits = []
    start = min(a, b)
    end = max(a, b)
    for i in range(start, end + 1):
        if i % 2 == 0:
            even_digits.append(i)
    return even_digits