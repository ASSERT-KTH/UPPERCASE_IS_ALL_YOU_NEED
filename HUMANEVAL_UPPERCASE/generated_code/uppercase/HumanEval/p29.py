from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ FILTER AN INPUT LIST OF STRINGS ONLY FOR ONES THAT START WITH A GIVEN PREFIX.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]