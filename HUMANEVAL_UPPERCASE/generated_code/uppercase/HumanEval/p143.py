def words_in_sentence(sentence):
    """
    YOU ARE GIVEN A STRING REPRESENTING A SENTENCE,
    THE SENTENCE CONTAINS SOME WORDS SEPARATED BY A SPACE,
    AND YOU HAVE TO RETURN A STRING THAT CONTAINS THE WORDS FROM THE ORIGINAL SENTENCE,
    WHOSE LENGTHS ARE PRIME NUMBERS,
    THE ORDER OF THE WORDS IN THE NEW STRING SHOULD BE THE SAME AS THE ORIGINAL ONE.

    EXAMPLE 1:
        INPUT: SENTENCE = "THIS IS A TEST"
        OUTPUT: "IS"

    EXAMPLE 2:
        INPUT: SENTENCE = "LETS GO FOR SWIMMING"
        OUTPUT: "GO FOR"

    CONSTRAINTS:
        * 1 <= LEN(SENTENCE) <= 100
        * SENTENCE CONTAINS ONLY LETTERS
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)