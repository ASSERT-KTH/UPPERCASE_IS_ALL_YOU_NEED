def sort_array(arr):
    """
    IN THIS KATA, YOU HAVE TO SORT AN ARRAY OF NON-NEGATIVE INTEGERS ACCORDING TO
    NUMBER OF ONES IN THEIR BINARY REPRESENTATION IN ASCENDING ORDER.
    FOR SIMILAR NUMBER OF ONES, SORT BASED ON DECIMAL VALUE.

    IT MUST BE IMPLEMENTED LIKE THIS:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    def count_ones(n):
        return bin(n).count('1')

    arr.sort(key=lambda x: (count_ones(abs(x)), x))
    return arr