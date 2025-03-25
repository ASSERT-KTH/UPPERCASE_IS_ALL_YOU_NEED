def is_palindrome(text: str):
    """
    CHECKS IF GIVEN STRING IS A PALINDROME
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    processed_text = ''.join(char.lower() for char in text if char.isalnum())
    return processed_text == processed_text[::-1]