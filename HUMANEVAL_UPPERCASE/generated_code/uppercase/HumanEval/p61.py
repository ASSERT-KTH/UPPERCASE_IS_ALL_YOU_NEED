def correct_bracketing(brackets: str):
    """ BRACKETS IS A STRING OF "(" AND ")".
    RETURN TRUE IF EVERY OPENING BRACKET HAS A CORRESPONDING CLOSING BRACKET.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    count = 0
    for bracket in brackets:
        if bracket == "(":
            count += 1
        elif bracket == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0