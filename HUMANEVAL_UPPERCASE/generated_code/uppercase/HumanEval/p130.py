def tri(n):
    """EVERYONE KNOWS FIBONACCI SEQUENCE, IT WAS STUDIED DEEPLY BY MATHEMATICIANS IN 
    THE LAST COUPLE CENTURIES. HOWEVER, WHAT PEOPLE DON'T KNOW IS TRIBONACCI SEQUENCE.
    TRIBONACCI SEQUENCE IS DEFINED BY THE RECURRENCE:
    TRI(1) = 3
    TRI(N) = 1 + N / 2, IF N IS EVEN.
    TRI(N) =  TRI(N - 1) + TRI(N - 2) + TRI(N + 1), IF N IS ODD.
    FOR EXAMPLE:
    TRI(2) = 1 + (2 / 2) = 2
    TRI(4) = 3
    TRI(3) = TRI(2) + TRI(1) + TRI(4)
           = 2 + 3 + 3 = 8 
    YOU ARE GIVEN A NON-NEGATIVE INTEGER NUMBER N, YOU HAVE TO A RETURN A LIST OF THE 
    FIRST N + 1 NUMBERS OF THE TRIBONACCI SEQUENCE.
    EXAMPLES:
    TRI(3) = [3, 2, 8, 3]
    """
    if n < 0:
        return []
    
    trib_sequence = []
    
    for i in range(n + 1):
        if i == 0:
            trib_sequence.append(3)
        elif i % 2 == 0:
            trib_sequence.append(1 + i / 2)
        else:
            if i < 2:
                trib_sequence.append(3 + 3 + (1 + (i+1) / 2 if (i+1) % 2 == 0 else 3))
            elif i ==1:
                trib_sequence.append(2  + 3 +  (1+(2/2)))
            else:
                trib_sequence.append(trib_sequence[i-1] + trib_sequence[i-2] + (1 + (i + 1) / 2 if (i + 1) % 2 == 0 else trib_sequence[i + 1] if (i+1) <= n else (1 + (i+1) / 2) ))
                
    return trib_sequence