def unique_digits(x):
    """GIVEN A LIST OF POSITIVE INTEGERS X. RETURN A SORTED LIST OF ALL 
    ELEMENTS THAT HASN'T ANY EVEN DIGIT.

    NOTE: RETURNED LIST SHOULD BE SORTED IN INCREASING ORDER.
    
    FOR EXAMPLE:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    result = []
    for num in x:
        s_num = str(num)
        has_even = False
        for digit in s_num:
            if int(digit) % 2 == 0:
                has_even = True
                break
        if not has_even:
            result.append(num)
    result.sort()
    return result