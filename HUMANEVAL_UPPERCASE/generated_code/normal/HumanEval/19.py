from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
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
    
    reverse_number_map = {v: k for k, v in number_map.items()}
    
    number_list = numbers.split()
    
    numerical_values = [number_map[number] for number in number_list]
    
    numerical_values.sort()
    
    sorted_numbers = [reverse_number_map[value] for value in numerical_values]
    
    return ' '.join(sorted_numbers)