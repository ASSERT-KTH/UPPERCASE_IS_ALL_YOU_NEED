def choose_num(x, y):
    """THIS FUNCTION TAKES TWO POSITIVE NUMBERS X AND Y AND RETURNS THE
    BIGGEST EVEN INTEGER NUMBER THAT IS IN THE RANGE [X, Y] INCLUSIVE. IF 
    THERE'S NO SUCH NUMBER, THEN THE FUNCTION SHOULD RETURN -1.

    FOR EXAMPLE:
    CHOOSE_NUM(12, 15) = 14
    CHOOSE_NUM(13, 12) = -1
    """
    if x > y:
        return -1

    for i in range(y, x - 1, -1):
        if i % 2 == 0:
            return i

    return -1