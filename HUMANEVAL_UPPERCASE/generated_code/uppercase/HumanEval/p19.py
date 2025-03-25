from typing import List


def sort_numbers(numbers: str) -> str:
    """ INPUT IS A SPACE-DELIMITED STRING OF NUMBERALS FROM 'ZERO' TO 'NINE'.
    VALID CHOICES ARE 'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT' AND 'NINE'.
    RETURN THE STRING WITH NUMBERS SORTED FROM SMALLEST TO LARGEST
    >>> sort_numbers('three one five')
    'one three five'
    """
    number_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    words = numbers.split()
    
    sorted_words = sorted(words, key=lambda word: number_map[word])
    
    return ' '.join(sorted_words)