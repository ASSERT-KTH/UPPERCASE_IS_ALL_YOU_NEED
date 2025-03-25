def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even_digits = []
    start = min(a, b)
    end = max(a, b)
    for i in range(start, end + 1):
        if i % 2 == 0:
            even_digits.append(i)
    return even_digits