def below_threshold(l: list, t: int):
    """RETURN TRUE IF ALL NUMBERS IN THE LIST L ARE BELOW THRESHOLD T.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for x in l:
        if x >= t:
            return False
    return True