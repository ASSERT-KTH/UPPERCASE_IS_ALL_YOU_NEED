def encode(message):
    """
    WRITE A FUNCTION THAT TAKES A MESSAGE, AND ENCODES IN SUCH A 
    WAY THAT IT SWAPS CASE OF ALL LETTERS, REPLACES ALL VOWELS IN 
    THE MESSAGE WITH THE LETTER THAT APPEARS 2 PLACES AHEAD OF THAT 
    VOWEL IN THE ENGLISH ALPHABET. 
    ASSUME ONLY LETTERS. 
    
    EXAMPLES:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for char in message:
        if 'a' <= char <= 'z':
            if char in vowels:
                index = vowels.find(char)
                encoded_message += chr(ord('a') + (index + 2) % 5)
            else:
                encoded_message += char.upper()
        elif 'A' <= char <= 'Z':
            if char in vowels:
                index = vowels.find(char)
                encoded_message += chr(ord('A') + (index + 2) % 5)
            else:
                encoded_message += char.lower()
        else:
            encoded_message += char  # Handle spaces or other non-letters
    return encoded_message