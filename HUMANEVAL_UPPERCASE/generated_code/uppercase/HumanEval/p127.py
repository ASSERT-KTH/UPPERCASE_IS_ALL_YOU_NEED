def intersection(interval1, interval2):
    """YOU ARE GIVEN TWO INTERVALS,
    WHERE EACH INTERVAL IS A PAIR OF INTEGERS. FOR EXAMPLE, INTERVAL = (START, END) = (1, 2).
    THE GIVEN INTERVALS ARE CLOSED WHICH MEANS THAT THE INTERVAL (START, END)
    INCLUDES BOTH START AND END.
    FOR EACH GIVEN INTERVAL, IT IS ASSUMED THAT ITS START IS LESS OR EQUAL ITS END.
    YOUR TASK IS TO DETERMINE WHETHER THE LENGTH OF INTERSECTION OF THESE TWO 
    INTERVALS IS A PRIME NUMBER.
    EXAMPLE, THE INTERSECTION OF THE INTERVALS (1, 3), (2, 4) IS (2, 3)
    WHICH ITS LENGTH IS 1, WHICH NOT A PRIME NUMBER.
    IF THE LENGTH OF THE INTERSECTION IS A PRIME NUMBER, RETURN "YES",
    OTHERWISE, RETURN "NO".
    IF THE TWO INTERVALS DON'T INTERSECT, RETURN "NO".


    [INPUT/OUTPUT] SAMPLES:
    INTERSECTION((1, 2), (2, 3)) ==> "NO"
    INTERSECTION((-1, 1), (0, 4)) ==> "NO"
    INTERSECTION((-3, -1), (-5, 5)) ==> "YES"
    """
    start1, end1 = interval1
    start2, end2 = interval2
    
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    
    if intersection_start < intersection_end:
        length = intersection_end - intersection_start
        if length <= 1:
            return "NO"
        
        for i in range(2, int(length**0.5) + 1):
            if length % i == 0:
                return "NO"
        return "YES"
    elif intersection_start == intersection_end:
        return "NO"
    else:
        return "NO"