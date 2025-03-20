from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ GIVEN LIST OF NUMBERS (OF AT LEAST TWO ELEMENTS), APPLY A LINEAR TRANSFORM TO THAT LIST,
    SUCH THAT THE SMALLEST NUMBER WILL BECOME 0 AND THE LARGEST WILL BECOME 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if not numbers:
        return []

    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:
        return [0.0] * len(numbers)  # Handle case where all numbers are the same

    rescaled_numbers = [(x - min_val) / (max_val - min_val) for x in numbers]
    return rescaled_numbers