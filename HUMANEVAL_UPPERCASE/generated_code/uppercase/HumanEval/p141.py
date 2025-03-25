import re

def file_name_check(file_name):
    """CREATE A FUNCTION WHICH TAKES A STRING REPRESENTING A FILE'S NAME, AND RETURNS
    'YES' IF THE THE FILE'S NAME IS VALID, AND RETURNS 'NO' OTHERWISE.
    A FILE'S NAME IS CONSIDERED TO BE VALID IF AND ONLY IF ALL THE FOLLOWING CONDITIONS 
    ARE MET:
    - THERE SHOULD NOT BE MORE THAN THREE DIGITS ('0'-'9') IN THE FILE'S NAME.
    - THE FILE'S NAME CONTAINS EXACTLY ONE DOT '.'
    - THE SUBSTRING BEFORE THE DOT SHOULD NOT BE EMPTY, AND IT STARTS WITH A LETTER FROM 
    THE LATIN ALPHAPET ('A'-'Z' AND 'A'-'Z').
    - THE SUBSTRING AFTER THE DOT SHOULD BE ONE OF THESE: ['TXT', 'EXE', 'DLL']
    EXAMPLES:
    FILE_NAME_CHECK("EXAMPLE.TXT") # => 'YES'
    FILE_NAME_CHECK("1EXAMPLE.DLL") # => 'NO' (THE NAME SHOULD START WITH A LATIN ALPHAPET LETTER)
    """

    # Check for digits
    digit_count = sum(1 for char in file_name if char.isdigit())
    if digit_count > 3:
        return 'NO'

    # Check for exactly one dot
    dot_count = file_name.count('.')
    if dot_count != 1:
        return 'NO'

    # Split the file name by the dot
    parts = file_name.split('.')
    if len(parts) != 2:  # Should only have two parts after splitting
        return 'NO'

    name, extension = parts
    
    # Check the name part
    if not name or not name[0].isalpha():
        return 'NO'
    
    # Check the extension
    if extension.upper() not in ['TXT', 'EXE', 'DLL']:
        return 'NO'

    return 'YES'