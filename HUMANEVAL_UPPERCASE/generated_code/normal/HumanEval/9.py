from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    
    result = []
    current_max = numbers[0]
    result.append(current_max)

    for i in range(1, len(numbers)):
        current_max = max(current_max, numbers[i])
        result.append(current_max)

    return result