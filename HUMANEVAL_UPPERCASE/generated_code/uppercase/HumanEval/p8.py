from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ FOR A GIVEN LIST OF INTEGERS, RETURN A TUPLE CONSISTING OF A SUM AND A PRODUCT OF ALL THE INTEGERS IN A LIST.
    EMPTY SUM SHOULD BE EQUAL TO 0 AND EMPTY PRODUCT SHOULD BE EQUAL TO 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum_of_numbers = 0
    product_of_numbers = 1
    for number in numbers:
        sum_of_numbers += number
        product_of_numbers *= number
    return (sum_of_numbers, product_of_numbers)