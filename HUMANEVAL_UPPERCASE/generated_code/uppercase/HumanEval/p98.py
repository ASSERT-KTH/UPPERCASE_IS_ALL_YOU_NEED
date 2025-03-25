def count_upper(s):
    """
    GIVEN A STRING S, COUNT THE NUMBER OF UPPERCASE VOWELS IN EVEN INDICES.
    
    FOR EXAMPLE:
    COUNT_UPPER('ABCDEF') RETURNS 1
    COUNT_UPPER('ABCDEFG') RETURNS 0
    COUNT_UPPER('DBBE') RETURNS 0
    """
    count = 0
    vowels = "AEIOU"
    for i in range(0, len(s), 2):
        if i < len(s) and s[i] in vowels and s[i].isupper():
            count += 1
    return count