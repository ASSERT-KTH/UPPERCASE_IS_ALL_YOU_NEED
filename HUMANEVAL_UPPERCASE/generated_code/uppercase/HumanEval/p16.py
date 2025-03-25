def count_distinct_characters(string: str) -> int:
    """ GIVEN A STRING, FIND OUT HOW MANY DISTINCT CHARACTERS (REGARDLESS OF CASE) DOES IT CONSIST OF
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_chars = set()
    for char in string.lower():
        distinct_chars.add(char)
    return len(distinct_chars)