from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ FROM A LIST OF INTEGERS, REMOVE ALL ELEMENTS THAT OCCUR MORE THAN ONCE.
    KEEP ORDER OF ELEMENTS LEFT THE SAME AS IN THE INPUT.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    counts = {}
    result = []
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    for number in numbers:
        if counts[number] == 1:
            result.append(number)
    return result