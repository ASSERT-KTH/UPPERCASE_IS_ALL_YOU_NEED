from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ FROM A GIVEN LIST OF INTEGERS, GENERATE A LIST OF ROLLING MAXIMUM ELEMENT FOUND UNTIL GIVEN MOMENT
    IN THE SEQUENCE.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    rolling_maximums = []
    current_max = numbers[0]
    rolling_maximums.append(current_max)

    for number in numbers[1:]:
        current_max = max(current_max, number)
        rolling_maximums.append(current_max)

    return rolling_maximums