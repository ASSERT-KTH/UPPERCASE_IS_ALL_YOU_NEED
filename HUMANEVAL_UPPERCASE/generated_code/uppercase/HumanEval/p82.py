def prime_length(string):
    """WRITE A FUNCTION THAT TAKES A STRING AND RETURNS TRUE IF THE STRING
    LENGTH IS A PRIME NUMBER OR FALSE OTHERWISE
    EXAMPLES
    PRIME_LENGTH('HELLO') == TRUE
    PRIME_LENGTH('ABCDCBA') == TRUE
    PRIME_LENGTH('KITTENS') == TRUE
    PRIME_LENGTH('ORANGE') == FALSE
    """

    length = len(string)
    if length <= 1:
        return False
    for i in range(2, int(length**0.5) + 1):
        if length % i == 0:
            return False
    return True