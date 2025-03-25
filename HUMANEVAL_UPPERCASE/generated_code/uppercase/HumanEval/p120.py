def maximum(arr, k):
    """
    GIVEN AN ARRAY ARR OF INTEGERS AND A POSITIVE INTEGER K, RETURN A SORTED LIST 
    OF LENGTH K WITH THE MAXIMUM K NUMBERS IN ARR.

    EXAMPLE 1:

        INPUT: ARR = [-3, -4, 5], K = 3
        OUTPUT: [-4, -3, 5]

    EXAMPLE 2:

        INPUT: ARR = [4, -4, 4], K = 2
        OUTPUT: [4, 4]

    EXAMPLE 3:

        INPUT: ARR = [-3, 2, 1, 2, -1, -2, 1], K = 1
        OUTPUT: [2]

    NOTE:
        1. THE LENGTH OF THE ARRAY WILL BE IN THE RANGE OF [1, 1000].
        2. THE ELEMENTS IN THE ARRAY WILL BE IN THE RANGE OF [-1000, 1000].
        3. 0 <= K <= LEN(ARR)
    """
    if k == 0:
        return []
    
    arr.sort()
    return arr[len(arr) - k:]