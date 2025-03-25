def count_nums(arr):
    """
    WRITE A FUNCTION COUNT_NUMS WHICH TAKES AN ARRAY OF INTEGERS AND RETURNS
    THE NUMBER OF ELEMENTS WHICH HAS A SUM OF DIGITS > 0.
    IF A NUMBER IS NEGATIVE, THEN ITS FIRST SIGNED DIGIT WILL BE NEGATIVE:
    E.G. -123 HAS SIGNED DIGITS -1, 2, AND 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    count = 0
    for num in arr:
        sum_digits = 0
        for digit in str(num):
            if digit == '-':
                sum_digits -= int(str(num)[1])
            else:
                sum_digits += int(digit)
        if sum_digits > 0:
            count += 1
    return count