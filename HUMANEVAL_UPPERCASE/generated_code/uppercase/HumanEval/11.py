from typing import List


def string_xor(a: str, b: str) -> str:
    """ INPUT ARE TWO STRINGS A AND B CONSISTING ONLY OF 1S AND 0S.
    PERFORM BINARY XOR ON THESE INPUTS AND RETURN RESULT ALSO AS A STRING.
    >>> string_xor('010', '110')
    '100'
    """
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result