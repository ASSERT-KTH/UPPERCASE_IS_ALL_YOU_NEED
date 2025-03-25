def flip_case(string: str) -> str:
    """ FOR A GIVEN STRING, FLIP LOWERCASE CHARACTERS TO UPPERCASE AND UPPERCASE TO LOWERCASE.
    >>> flip_case('Hello')
    'hELLO'
    """
    flipped_string = ''
    for char in string:
        if 'a' <= char <= 'z':
            flipped_string += char.upper()
        elif 'A' <= char <= 'Z':
            flipped_string += char.lower()
        else:
            flipped_string += char
    return flipped_string