def smallest_change(arr):
    """
    GIVEN AN ARRAY ARR OF INTEGERS, FIND THE MINIMUM NUMBER OF ELEMENTS THAT
    NEED TO BE CHANGED TO MAKE THE ARRAY PALINDROMIC. A PALINDROMIC ARRAY IS AN ARRAY THAT
    IS READ THE SAME BACKWARDS AND FORWARDS. IN ONE CHANGE, YOU CAN CHANGE ONE ELEMENT TO ANY OTHER ELEMENT.

    FOR EXAMPLE:
    SMALLEST_CHANGE([1,2,3,5,4,7,9,6]) == 4
    SMALLEST_CHANGE([1, 2, 3, 4, 3, 2, 2]) == 1
    SMALLEST_CHANGE([1, 2, 3, 2, 1]) == 0
    """
    n = len(arr)
    changes = 0
    for i in range(n // 2):
        if arr[i] != arr[n - 1 - i]:
            changes += 1
    return changes