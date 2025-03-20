from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ INPUT TO THIS FUNCTION IS A STRING REPRESENTED MULTIPLE GROUPS FOR NESTED PARENTHESES SEPARATED BY SPACES.
    FOR EACH OF THE GROUP, OUTPUT THE DEEPEST LEVEL OF NESTING OF PARENTHESES.
    E.G. (()()) HAS MAXIMUM TWO LEVELS OF NESTING WHILE ((())) HAS THREE.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split()
    result = []
    for group in groups:
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        result.append(max_depth)
    return result