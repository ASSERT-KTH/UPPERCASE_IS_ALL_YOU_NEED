def histogram(test):
    """GIVEN A STRING REPRESENTING A SPACE SEPARATED LOWERCASE LETTERS, RETURN A DICTIONARY
    OF THE LETTER WITH THE MOST REPETITION AND CONTAINING THE CORRESPONDING COUNT.
    IF SEVERAL LETTERS HAVE THE SAME OCCURRENCE, RETURN ALL OF THEM.
    
    EXAMPLE:
    HISTOGRAM('A B C') == {'A': 1, 'B': 1, 'C': 1}
    HISTOGRAM('A B B A') == {'A': 2, 'B': 2}
    HISTOGRAM('A B C A B') == {'A': 2, 'B': 2}
    HISTOGRAM('B B B B A') == {'B': 4}
    HISTOGRAM('') == {}

    """
    counts = {}
    if not test:
        return {}
    letters = test.split()
    for letter in letters:
        counts[letter] = counts.get(letter, 0) + 1
    
    if not counts:
        return {}

    max_count = max(counts.values())
    result = {letter: count for letter, count in counts.items() if count == max_count}
    return result