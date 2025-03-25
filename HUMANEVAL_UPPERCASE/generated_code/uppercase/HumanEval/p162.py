import hashlib

def string_to_md5(text):
    """
    GIVEN A STRING 'TEXT', RETURN ITS MD5 HASH EQUIVALENT STRING.
    IF 'TEXT' IS AN EMPTY STRING, RETURN NONE.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    else:
        return hashlib.md5(text.encode()).hexdigest()