def even_odd_palindrome(n):
    """
    GIVEN A POSITIVE INTEGER N, RETURN A TUPLE THAT HAS THE NUMBER OF EVEN AND ODD
    INTEGER PALINDROMES THAT FALL WITHIN THE RANGE(1, N), INCLUSIVE.

    EXAMPLE 1:

        INPUT: 3
        OUTPUT: (1, 2)
        EXPLANATION:
        INTEGER PALINDROME ARE 1, 2, 3. ONE OF THEM IS EVEN, AND TWO OF THEM ARE ODD.

    EXAMPLE 2:

        INPUT: 12
        OUTPUT: (4, 6)
        EXPLANATION:
        INTEGER PALINDROME ARE 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. FOUR OF THEM ARE EVEN, AND 6 OF THEM ARE ODD.

    NOTE:
        1. 1 <= N <= 10^3
        2. RETURNED TUPLE HAS THE NUMBER OF EVEN AND ODD INTEGER PALINDROMES RESPECTIVELY.
    """
    even_count = 0
    odd_count = 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)