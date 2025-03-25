def add(lst):
    """GIVEN A NON-EMPTY LIST OF INTEGERS LST. ADD THE EVEN ELEMENTS THAT ARE AT ODD INDICES..


    EXAMPLES:
        ADD([4, 2, 6, 7]) ==> 2 
    """
    sum = 0
    for i in range(len(lst)):
        if i % 2 != 0 and lst[i] % 2 == 0:
            sum += lst[i]
    return sum