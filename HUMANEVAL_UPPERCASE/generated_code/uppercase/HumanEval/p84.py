def solve(N):
    """GIVEN A POSITIVE INTEGER N, RETURN THE TOTAL SUM OF ITS DIGITS IN BINARY.
    
    EXAMPLE
        FOR N = 1000, THE SUM OF DIGITS WILL BE 1 THE OUTPUT SHOULD BE "1".
        FOR N = 150, THE SUM OF DIGITS WILL BE 6 THE OUTPUT SHOULD BE "110".
        FOR N = 147, THE SUM OF DIGITS WILL BE 12 THE OUTPUT SHOULD BE "1100".
    
    VARIABLES:
        @N INTEGER
             CONSTRAINTS: 0 ≤ N ≤ 10000.
    OUTPUT:
         A STRING OF BINARY NUMBER
    """
    # Calculate the sum of digits
    sum_digits = sum(int(digit) for digit in str(N))

    # Convert the sum to binary
    binary_representation = bin(sum_digits)[2:]

    return binary_representation