def order_by_points(nums):
    """
    WRITE A FUNCTION WHICH SORTS THE GIVEN LIST OF INTEGERS
    IN ASCENDING ORDER ACCORDING TO THE SUM OF THEIR DIGITS.
    NOTE: IF THERE ARE SEVERAL ITEMS WITH SIMILAR SUM OF THEIR DIGITS,
    ORDER THEM BASED ON THEIR INDEX IN ORIGINAL LIST.

    FOR EXAMPLE:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    def sum_of_digits(n):
        s = 0
        for digit in str(abs(n)):
            s += int(digit)
        return s

    indexed_nums = list(enumerate(nums))
    indexed_nums.sort(key=lambda x: (sum_of_digits(x[1]), x[0]))
    return [num for _, num in indexed_nums]