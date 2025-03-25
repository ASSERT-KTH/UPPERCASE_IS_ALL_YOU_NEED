def select_words(s, n):
    """GIVEN A STRING S AND A NATURAL NUMBER N, YOU HAVE BEEN TASKED TO IMPLEMENT 
    A FUNCTION THAT RETURNS A LIST OF ALL WORDS FROM STRING S THAT CONTAIN EXACTLY 
    N CONSONANTS, IN ORDER THESE WORDS APPEAR IN THE STRING S.
    IF THE STRING S IS EMPTY THEN THE FUNCTION SHOULD RETURN AN EMPTY LIST.
    NOTE: YOU MAY ASSUME THE INPUT STRING CONTAINS ONLY LETTERS AND SPACES.
    EXAMPLES:
    SELECT_WORDS("MARY HAD A LITTLE LAMB", 4) ==> ["LITTLE"]
    SELECT_WORDS("MARY HAD A LITTLE LAMB", 3) ==> ["MARY", "LAMB"]
    SELECT_WORDS("SIMPLE WHITE SPACE", 2) ==> []
    SELECT_WORDS("HELLO WORLD", 4) ==> ["WORLD"]
    SELECT_WORDS("UNCLE SAM", 3) ==> ["UNCLE"]
    """
    if not s:
        return []

    vowels = "AEIOUaeiou"
    result = []
    words = s.split()

    for word in words:
        consonant_count = 0
        for char in word:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':  # Check if it's a letter
              if char not in vowels:
                consonant_count += 1
        if consonant_count == n:
            result.append(word)
    
    return result