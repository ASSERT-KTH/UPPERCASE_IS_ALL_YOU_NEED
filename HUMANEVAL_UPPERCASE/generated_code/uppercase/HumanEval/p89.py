def encrypt(s):
    """CREATE A FUNCTION ENCRYPT THAT TAKES A STRING AS AN ARGUMENT AND
    RETURNS A STRING ENCRYPTED WITH THE ALPHABET BEING ROTATED. 
    THE ALPHABET SHOULD BE ROTATED IN A MANNER SUCH THAT THE LETTERS 
    SHIFT DOWN BY TWO MULTIPLIED TO TWO PLACES.
    FOR EXAMPLE:
    ENCRYPT('HI') RETURNS 'LM'
    ENCRYPT('ASDFGHJKL') RETURNS 'EWHJKLNOP'
    ENCRYPT('GF') RETURNS 'KJ'
    ENCRYPT('ET') RETURNS 'IX'
    """
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            shifted_char = chr(((ord(char) - ord('a') + 4) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            shifted_char = chr(((ord(char) - ord('A') + 4) % 26) + ord('A'))
        else:
            shifted_char = char
        result += shifted_char
    return result