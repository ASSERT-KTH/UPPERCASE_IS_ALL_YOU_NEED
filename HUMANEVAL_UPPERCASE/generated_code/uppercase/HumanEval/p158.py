def find_max(words):
    """WRITE A FUNCTION THAT ACCEPTS A LIST OF STRINGS.
    THE LIST CONTAINS DIFFERENT WORDS. RETURN THE WORD WITH MAXIMUM NUMBER
    OF UNIQUE CHARACTERS. IF MULTIPLE STRINGS HAVE MAXIMUM NUMBER OF UNIQUE
    CHARACTERS, RETURN THE ONE WHICH COMES FIRST IN LEXICOGRAPHICAL ORDER.

    FIND_MAX(["NAME", "OF", "STRING"]) == "STRING"
    FIND_MAX(["NAME", "ENAM", "GAME"]) == "ENAM"
    FIND_MAX(["AAAAAAA", "BB" ,"CC"]) == ""AAAAAAA"
    """
    if not words:
        return ""

    max_unique_chars = -1
    result = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            result = word
        elif unique_chars == max_unique_chars:
            if word < result:
                result = word

    return result