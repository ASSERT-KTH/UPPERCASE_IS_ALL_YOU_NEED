def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    largest_negative = None
    smallest_positive = None

    negative_integers = [num for num in lst if num < 0]
    positive_integers = [num for num in lst if num > 0]

    if negative_integers:
        largest_negative = max(negative_integers)
    if positive_integers:
        smallest_positive = min(positive_integers)

    return (largest_negative, smallest_positive)