def exchange(lst1, lst2):
    """IN THIS PROBLEM, YOU WILL IMPLEMENT A FUNCTION THAT TAKES TWO LISTS OF NUMBERS,
    AND DETERMINES WHETHER IT IS POSSIBLE TO PERFORM AN EXCHANGE OF ELEMENTS
    BETWEEN THEM TO MAKE LST1 A LIST OF ONLY EVEN NUMBERS.
    THERE IS NO LIMIT ON THE NUMBER OF EXCHANGED ELEMENTS BETWEEN LST1 AND LST2.
    IF IT IS POSSIBLE TO EXCHANGE ELEMENTS BETWEEN THE LST1 AND LST2 TO MAKE
    ALL THE ELEMENTS OF LST1 TO BE EVEN, RETURN "YES".
    OTHERWISE, RETURN "NO".
    FOR EXAMPLE:
    EXCHANGE([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    EXCHANGE([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    IT IS ASSUMED THAT THE INPUT LISTS WILL BE NON-EMPTY.
    """
    odd_in_lst1 = 0
    for num in lst1:
        if num % 2 != 0:
            odd_in_lst1 += 1
    
    odd_in_lst2 = 0
    for num in lst2:
        if num % 2 != 0:
            odd_in_lst2 += 1
            
    if odd_in_lst1 <= odd_in_lst2:
        return "YES"
    else:
        return "NO"