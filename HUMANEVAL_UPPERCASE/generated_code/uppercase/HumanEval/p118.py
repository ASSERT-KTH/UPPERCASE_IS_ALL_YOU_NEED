def get_closest_vowel(word):
    """YOU ARE GIVEN A WORD. YOUR TASK IS TO FIND THE CLOSEST VOWEL THAT STANDS BETWEEN 
    TWO CONSONANTS FROM THE RIGHT SIDE OF THE WORD (CASE SENSITIVE).
    
    VOWELS IN THE BEGINNING AND ENDING DOESN'T COUNT. RETURN EMPTY STRING IF YOU DIDN'T
    FIND ANY VOWEL MET THE ABOVE CONDITION. 

    YOU MAY ASSUME THAT THE GIVEN STRING CONTAINS ENGLISH LETTER ONLY.

    EXAMPLE:
    GET_CLOSEST_VOWEL("YOGURT") ==> "U"
    GET_CLOSEST_VOWEL("FULL") ==> "U"
    GET_CLOSEST_VOWEL("QUICK") ==> ""
    GET_CLOSEST_VOWEL("AB") ==> ""
    """
    vowels = "AEIOUaeiou"
    n = len(word)
    for i in range(n - 2, 0, -1):
        if word[i] in vowels:
            if (word[i-1] not in vowels) and (word[i+1] not in vowels):
                return word[i]
    return ""