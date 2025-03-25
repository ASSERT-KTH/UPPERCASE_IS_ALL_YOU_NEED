def monotonic(l: list):
    """RETURN TRUE IS LIST ELEMENTS ARE MONOTONICALLY INCREASING OR DECREASING.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    increasing = True
    decreasing = True
    for i in range(len(l) - 1):
        if l[i] > l[i+1]:
            increasing = False
        if l[i] < l[i+1]:
            decreasing = False
    return increasing or decreasing