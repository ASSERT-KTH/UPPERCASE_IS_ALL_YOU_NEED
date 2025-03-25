def how_many_times(string: str, substring: str) -> int:
    """ FIND HOW MANY TIMES A GIVEN SUBSTRING CAN BE FOUND IN THE ORIGINAL STRING. COUNT OVERLAPING CASES.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not substring:
        return 0
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count