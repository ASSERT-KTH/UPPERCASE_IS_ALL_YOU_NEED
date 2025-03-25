from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if not numbers or len(numbers) < 2:
        return numbers

    min_val = min(numbers)
    max_val = max(numbers)
    if max_val == min_val:
        return [0.0] * len(numbers)

    rescaled_numbers = [(x - min_val) / (max_val - min_val) for x in numbers]
    return rescaled_numbers