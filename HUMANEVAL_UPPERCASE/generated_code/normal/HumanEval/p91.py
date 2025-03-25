def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    sentences = []
    sentence = ""
    for char in S:
        if char in ['.', '?', '!']:
            sentence += char
            sentences.append(sentence.strip())
            sentence = ""
        else:
            sentence += char
    if sentence:
        sentences.append(sentence.strip())
    
    count = 0
    for sentence in sentences:
        words = sentence.split()
        if len(words) > 0 and words[0] == "I":
            count += 1
    return count