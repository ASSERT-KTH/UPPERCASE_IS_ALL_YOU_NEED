FIX = """
ADD MORE TEST CASES.
"""

def vowels_count(s):
    """WRITE A FUNCTION VOWELS_COUNT WHICH TAKES A STRING REPRESENTING
    A WORD AS INPUT AND RETURNS THE NUMBER OF VOWELS IN THE STRING.
    VOWELS IN THIS CASE ARE 'A', 'E', 'I', 'O', 'U'. HERE, 'Y' IS ALSO A
    VOWEL, BUT ONLY WHEN IT IS AT THE END OF THE GIVEN WORD.

    EXAMPLE:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = "aeiouAEIOU"
    count = 0
    for i, char in enumerate(s):
        if char in vowels:
            count += 1
        elif char == 'y' or char == 'Y' and i == len(s) - 1:
            count +=1
    return count