from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ INPUT TO THIS FUNCTION IS A STRING CONTAINING MULTIPLE GROUPS OF NESTED PARENTHESES. YOUR GOAL IS TO
    SEPARATE THOSE GROUP INTO SEPARATE STRINGS AND RETURN THE LIST OF THOSE.
    SEPARATE GROUPS ARE BALANCED (EACH OPEN BRACE IS PROPERLY CLOSED) AND NOT NESTED WITHIN EACH OTHER
    IGNORE ANY SPACES IN THE INPUT STRING.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(" ", "")
    result = []
    start = 0
    balance = 0
    for i, char in enumerate(paren_string):
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance == 0 and char == ')':
            result.append(paren_string[start:i+1])
            start = i + 1
    return result