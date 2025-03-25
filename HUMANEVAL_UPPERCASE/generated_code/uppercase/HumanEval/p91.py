def is_bored(S):
    """
    YOU'LL BE GIVEN A STRING OF WORDS, AND YOUR TASK IS TO COUNT THE NUMBER
    OF BOREDOMS. A BOREDOM IS A SENTENCE THAT STARTS WITH THE WORD "I".
    SENTENCES ARE DELIMITED BY '.', '?' OR '!'.
   
    FOR EXAMPLE:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    sentences = []
    for delimiter in ['.', '?', '!']:
        S = S.replace(delimiter, delimiter + '*')
    sentences = [sentence.strip() for sentence in S.split('*') if sentence.strip()]
    
    count = 0
    for sentence in sentences:
        if sentence.startswith("I "):
            count += 1
        elif sentence == "I":
            count +=1
    return count