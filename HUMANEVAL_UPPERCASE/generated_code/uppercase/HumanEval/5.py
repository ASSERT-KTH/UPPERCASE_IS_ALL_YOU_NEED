from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ INSERT A NUMBER 'DELIMETER' BETWEEN EVERY TWO CONSECUTIVE ELEMENTS OF INPUT LIST `NUMBERS'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    result = [numbers[0]]
    for num in numbers[1:]:
        result.append(delimeter)
        result.append(num)
    return result