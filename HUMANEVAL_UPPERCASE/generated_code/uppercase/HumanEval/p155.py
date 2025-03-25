def even_odd_count(num):
    """GIVEN AN INTEGER. RETURN A TUPLE THAT HAS THE NUMBER OF EVEN AND ODD DIGITS RESPECTIVELY.

     EXAMPLE:
        EVEN_ODD_COUNT(-12) ==> (1, 1)
        EVEN_ODD_COUNT(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    num_str = str(abs(num))  # Handle negative numbers and convert to string
    for digit_char in num_str:
        digit = int(digit_char)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)