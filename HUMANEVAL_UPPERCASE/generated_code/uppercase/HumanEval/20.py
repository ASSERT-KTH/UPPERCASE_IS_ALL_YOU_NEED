from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ FROM A SUPPLIED LIST OF NUMBERS (OF LENGTH AT LEAST TWO) SELECT AND RETURN TWO THAT ARE THE CLOSEST TO EACH
    OTHER AND RETURN THEM IN ORDER (SMALLER NUMBER, LARGER NUMBER).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    closest_pair = (numbers[0], numbers[1])
    min_diff = abs(numbers[0] - numbers[1])

    for i in range(1, len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i+1])
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i+1])
    
    return (min(closest_pair[0], closest_pair[1]), max(closest_pair[0], closest_pair[1]))