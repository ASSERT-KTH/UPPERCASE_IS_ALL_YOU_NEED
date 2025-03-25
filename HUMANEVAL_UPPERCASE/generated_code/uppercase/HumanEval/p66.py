def digitSum(s):
    """TASK
    WRITE A FUNCTION THAT TAKES A STRING AS INPUT AND RETURNS THE SUM OF THE UPPER CHARACTERS ONLY'
    ASCII CODES.

    EXAMPLES:
        DIGITSUM("") => 0
        DIGITSUM("ABAB") => 131
        DIGITSUM("ABCCD") => 67
        DIGITSUM("HELLOE") => 69
        DIGITSUM("WOARBLD") => 131
        DIGITSUM("AAAAAXA") => 153
    """
    sum_of_upper_chars = 0
    for char in s:
        if 'A' <= char <= 'Z':
            sum_of_upper_chars += ord(char)
    return sum_of_upper_chars