def encode_shift(s: str):
    """
    RETURNS ENCODED STRING BY SHIFTING EVERY CHARACTER BY 5 IN THE ALPHABET.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    TAKES AS INPUT STRING ENCODED WITH ENCODE_SHIFT FUNCTION. RETURNS DECODED STRING.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])