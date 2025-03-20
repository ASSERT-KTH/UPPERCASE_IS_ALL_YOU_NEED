def is_palindrome(string: str) -> bool:
    """ TEST IF GIVEN STRING IS A PALINDROME """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ FIND THE SHORTEST PALINDROME THAT BEGINS WITH A SUPPLIED STRING.
    ALGORITHM IDEA IS SIMPLE:
    - FIND THE LONGEST POSTFIX OF SUPPLIED STRING THAT IS A PALINDROME.
    - APPEND TO THE END OF THE STRING REVERSE OF A STRING PREFIX THAT COMES BEFORE THE PALINDROMIC SUFFIX.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ""

    for i in range(len(string)):
        if is_palindrome(string[i:]):
            prefix = string[:i]
            return string + prefix[::-1]