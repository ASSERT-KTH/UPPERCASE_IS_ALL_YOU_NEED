def anti_shuffle(s):
    """
    WRITE A FUNCTION THAT TAKES A STRING AND RETURNS AN ORDERED VERSION OF IT.
    ORDERED VERSION OF STRING, IS A STRING WHERE ALL WORDS (SEPARATED BY SPACE)
    ARE REPLACED BY A NEW WORD WHERE ALL THE CHARACTERS ARRANGED IN
    ASCENDING ORDER BASED ON ASCII VALUE.
    NOTE: YOU SHOULD KEEP THE ORDER OF WORDS AND BLANK SPACES IN THE SENTENCE.

    FOR EXAMPLE:
    ANTI_SHUFFLE('HI') RETURNS 'HI'
    ANTI_SHUFFLE('HELLO') RETURNS 'EHLLO'
    ANTI_SHUFFLE('HELLO WORLD!!!') RETURNS 'EHLLO !!!DLORW'
    """
    words = s.split()
    ordered_words = []
    for word in words:
        ordered_word = ''.join(sorted(word))
        ordered_words.append(ordered_word)
    
    # Reconstruct the string, preserving spaces
    result = ""
    word_index = 0
    for i in range(len(s)):
        if i < len(s) and i < len(s) - 1 and s[i] == ' ' :
            result += ' '
        elif s[i] != ' ':
            result += ordered_words[word_index][0]
            ordered_words[word_index] = ordered_words[word_index][1:] 
            if not ordered_words[word_index]:
                word_index +=1
    return result