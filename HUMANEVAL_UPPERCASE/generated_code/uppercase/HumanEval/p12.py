from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ OUT OF LIST OF STRINGS, RETURN THE LONGEST ONE. RETURN THE FIRST ONE IN CASE OF MULTIPLE
    STRINGS OF THE SAME LENGTH. RETURN NONE IN CASE THE INPUT LIST IS EMPTY.
    >>> longest([])
    None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None

    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string