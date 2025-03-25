def words_string(s):
    """
    YOU WILL BE GIVEN A STRING OF WORDS SEPARATED BY COMMAS OR SPACES. YOUR TASK IS
    TO SPLIT THE STRING INTO WORDS AND RETURN AN ARRAY OF THE WORDS.
    
    FOR EXAMPLE:
    WORDS_STRING("HI, MY NAME IS JOHN") == ["HI", "MY", "NAME", "IS", "JOHN"]
    WORDS_STRING("ONE, TWO, THREE, FOUR, FIVE, SIX") == ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"]
    """
    words = s.replace(",", " ").split()
    return words