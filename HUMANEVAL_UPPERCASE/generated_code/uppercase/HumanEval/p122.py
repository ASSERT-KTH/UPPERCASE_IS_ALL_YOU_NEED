def add_elements(arr, k):
    """
    GIVEN A NON-EMPTY ARRAY OF INTEGERS ARR AND AN INTEGER K, RETURN
    THE SUM OF THE ELEMENTS WITH AT MOST TWO DIGITS FROM THE FIRST K ELEMENTS OF ARR.

    EXAMPLE:

        INPUT: ARR = [111,21,3,4000,5,6,7,8,9], K = 4
        OUTPUT: 24 # SUM OF 21 + 3

    CONSTRAINTS:
        1. 1 <= LEN(ARR) <= 100
        2. 1 <= K <= LEN(ARR)
    """
    sum_of_elements = 0
    for i in range(k):
        if 10 <= abs(arr[i]) <= 99 or abs(arr[i]) < 10:
            sum_of_elements += arr[i]
    return sum_of_elements