from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ FOR A GIVEN LIST OF INPUT NUMBERS, CALCULATE MEAN ABSOLUTE DEVIATION
    AROUND THE MEAN OF THIS DATASET.
    MEAN ABSOLUTE DEVIATION IS THE AVERAGE ABSOLUTE DIFFERENCE BETWEEN EACH
    ELEMENT AND A CENTERPOINT (MEAN IN THIS CASE):
    MAD = AVERAGE | X - X_MEAN |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    if not numbers:
        return 0.0

    mean = sum(numbers) / len(numbers)
    absolute_deviations = [abs(x - mean) for x in numbers]
    mad = sum(absolute_deviations) / len(numbers)
    return mad