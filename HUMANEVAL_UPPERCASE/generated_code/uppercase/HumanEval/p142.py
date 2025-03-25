def sum_squares(lst):
    """
    THIS FUNCTION WILL TAKE A LIST OF INTEGERS. FOR ALL ENTRIES IN THE LIST, THE FUNCTION SHALL SQUARE THE INTEGER ENTRY IF ITS INDEX IS A 
    MULTIPLE OF 3 AND WILL CUBE THE INTEGER ENTRY IF ITS INDEX IS A MULTIPLE OF 4 AND NOT A MULTIPLE OF 3. THE FUNCTION WILL NOT 
    CHANGE THE ENTRIES IN THE LIST WHOSE INDEXES ARE NOT A MULTIPLE OF 3 OR 4. THE FUNCTION SHALL THEN RETURN THE SUM OF ALL ENTRIES. 
    
    EXAMPLES:
    FOR LST = [1,2,3] THE OUTPUT SHOULD BE 6
    FOR LST = []  THE OUTPUT SHOULD BE 0
    FOR LST = [-1,-5,2,-1,-5]  THE OUTPUT SHOULD BE -126
    """
    sum_val = 0
    for i in range(len(lst)):
        if i % 3 == 0 and i % 4 != 0:
            sum_val += lst[i]**2
        elif i % 4 == 0 and i % 3 != 0:
            sum_val += lst[i]**3
        elif i % 3 == 0 and i % 4 == 0:
            sum_val += lst[i]**2
        else:
            sum_val += lst[i]
    return sum_val