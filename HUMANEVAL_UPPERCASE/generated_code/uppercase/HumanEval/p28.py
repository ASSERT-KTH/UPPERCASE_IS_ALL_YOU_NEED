from typing import List


def concatenate(strings: List[str]) -> str:
    """ CONCATENATE LIST OF STRINGS INTO A SINGLE STRING
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return "".join(strings)