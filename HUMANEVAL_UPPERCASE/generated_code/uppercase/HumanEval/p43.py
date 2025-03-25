def pairs_sum_to_zero(l):
    """
    PAIRS_SUM_TO_ZERO TAKES A LIST OF INTEGERS AS AN INPUT.
    IT RETURNS TRUE IF THERE ARE TWO DISTINCT ELEMENTS IN THE LIST THAT
    SUM TO ZERO, AND FALSE OTHERWISE.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    seen = set()
    for x in l:
        if -x in seen:
            return True
        seen.add(x)
    return False