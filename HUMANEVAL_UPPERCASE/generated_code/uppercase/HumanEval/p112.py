def reverse_delete(s,c):
    """TASK
    WE ARE GIVEN TWO STRINGS S AND C, YOU HAVE TO DELETED ALL THE CHARACTERS IN S THAT ARE EQUAL TO ANY CHARACTER IN C
    THEN CHECK IF THE RESULT STRING IS PALINDROME.
    A STRING IS CALLED PALINDROME IF IT READS THE SAME BACKWARD AS FORWARD.
    YOU SHOULD RETURN A TUPLE CONTAINING THE RESULT STRING AND TRUE/FALSE FOR THE CHECK.
    EXAMPLE
    FOR S = "ABCDE", C = "AE", THE RESULT SHOULD BE ('BCD',FALSE)
    FOR S = "ABCDEF", C = "B"  THE RESULT SHOULD BE ('ACDEF',FALSE)
    FOR S = "ABCDEDCBA", C = "AB", THE RESULT SHOULD BE ('CDEDC',TRUE)
    """
    new_s = ""
    for char in s:
        if char not in c:
            new_s += char
    
    is_palindrome = new_s == new_s[::-1]
    
    return (new_s, is_palindrome)