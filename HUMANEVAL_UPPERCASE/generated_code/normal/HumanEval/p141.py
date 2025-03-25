import re

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    # Check for digits
    digit_count = sum(1 for char in file_name if char.isdigit())
    if digit_count > 3:
        return 'No'
    
    # Check for exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Split the file name by the dot
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'

    name_part = parts[0]
    extension_part = parts[1]

    # Check if the name part is not empty and starts with a letter
    if not name_part or not name_part[0].isalpha():
        return 'No'
    
    # Check if the extension is valid
    if extension_part not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'