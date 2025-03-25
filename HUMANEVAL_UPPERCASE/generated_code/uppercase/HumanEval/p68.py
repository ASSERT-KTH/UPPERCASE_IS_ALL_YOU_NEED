def pluck(arr):
    """
    "GIVEN AN ARRAY REPRESENTING A BRANCH OF A TREE THAT HAS NON-NEGATIVE INTEGER NODES
    YOUR TASK IS TO PLUCK ONE OF THE NODES AND RETURN IT.
    THE PLUCKED NODE SHOULD BE THE NODE WITH THE SMALLEST EVEN VALUE.
    IF MULTIPLE NODES WITH THE SAME SMALLEST EVEN VALUE ARE FOUND RETURN THE NODE THAT HAS SMALLEST INDEX.

    THE PLUCKED NODE SHOULD BE RETURNED IN A LIST, [ SMALEST_VALUE, ITS INDEX ],
    IF THERE ARE NO EVEN VALUES OR THE GIVEN ARRAY IS EMPTY, RETURN [].

    EXAMPLE 1:
        INPUT: [4,2,3]
        OUTPUT: [2, 1]
        EXPLANATION: 2 HAS THE SMALLEST EVEN VALUE, AND 2 HAS THE SMALLEST INDEX.

    EXAMPLE 2:
        INPUT: [1,2,3]
        OUTPUT: [2, 1]
        EXPLANATION: 2 HAS THE SMALLEST EVEN VALUE, AND 2 HAS THE SMALLEST INDEX. 

    EXAMPLE 3:
        INPUT: []
        OUTPUT: []
    
    EXAMPLE 4:
        INPUT: [5, 0, 3, 0, 4, 2]
        OUTPUT: [0, 1]
        EXPLANATION: 0 IS THE SMALLEST VALUE, BUT  THERE ARE TWO ZEROS,
                     SO WE WILL CHOOSE THE FIRST ZERO, WHICH HAS THE SMALLEST INDEX.

    CONSTRAINTS:
        * 1 <= NODES.LENGTH <= 10000
        * 0 <= NODE.VALUE
    """
    if not arr:
        return []
    
    min_even = float('inf')
    min_index = -1

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            if arr[i] < min_even:
                min_even = arr[i]
                min_index = i

    if min_index == -1:
        return []
    else:
        return [min_even, min_index]