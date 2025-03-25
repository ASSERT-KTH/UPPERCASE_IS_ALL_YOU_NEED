from typing import List


def below_zero(operations: List[int]) -> bool:
    """ YOU'RE GIVEN A LIST OF DEPOSIT AND WITHDRAWAL OPERATIONS ON A BANK ACCOUNT THAT STARTS WITH
    ZERO BALANCE. YOUR TASK IS TO DETECT IF AT ANY POINT THE BALANCE OF ACCOUNT FALLLS BELOW ZERO, AND
    AT THAT POINT FUNCTION SHOULD RETURN TRUE. OTHERWISE IT SHOULD RETURN FALSE.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False