def correct_bracketing(brackets: str):
    """ BRACKETS IS A STRING OF "<" AND ">".
    RETURN TRUE IF EVERY OPENING BRACKET HAS A CORRESPONDING CLOSING BRACKET.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    balance = 0
    for bracket in brackets:
        if bracket == "<":
            balance += 1
        elif bracket == ">":
            balance -= 1
        if balance < 0:
            return False
    return balance == 0