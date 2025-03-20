from typing import List


def all_prefixes(string: str) -> List[str]:
    """ RETURN LIST OF ALL PREFIXES FROM SHORTEST TO LONGEST OF THE INPUT STRING
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes