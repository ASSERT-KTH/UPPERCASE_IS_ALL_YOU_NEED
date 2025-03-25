def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    words = s.split()
    ordered_words = []
    for word in words:
        ordered_word = ''.join(sorted(word))
        ordered_words.append(ordered_word)
    
    # Reconstruct the sentence with spaces
    result = ""
    word_index = 0
    for i in range(len(s)):
        if i == 0 or s[i-1] == ' ':
            if word_index < len(ordered_words):
                result += ordered_words[word_index]
                word_index += 1
        elif s[i] != ' ':
            continue
        else:
            result += " "

    return result