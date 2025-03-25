def next_smallest(lst):
    """
    YOU ARE GIVEN A LIST OF INTEGERS.
    WRITE A FUNCTION NEXT_SMALLEST() THAT RETURNS THE 2ND SMALLEST ELEMENT OF THE LIST.
    RETURN NONE IF THERE IS NO SUCH ELEMENT.
    
    NEXT_SMALLEST([1, 2, 3, 4, 5]) == 2
    NEXT_SMALLEST([5, 1, 4, 3, 2]) == 2
    NEXT_SMALLEST([]) == NONE
    NEXT_SMALLEST([1, 1]) == NONE
    """
    if len(lst) < 2:
        return None
    
    unique_sorted_lst = sorted(list(set(lst)))
    
    if len(unique_sorted_lst) < 2:
        return None
    else:
        return unique_sorted_lst[1]