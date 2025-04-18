def decimal_to_binary(decimal):
    """YOU WILL BE GIVEN A NUMBER IN DECIMAL FORM AND YOUR TASK IS TO CONVERT IT TO
    BINARY FORMAT. THE FUNCTION SHOULD RETURN A STRING, WITH EACH CHARACTER REPRESENTING A BINARY
    NUMBER. EACH CHARACTER IN THE STRING WILL BE '0' OR '1'.

    THERE WILL BE AN EXTRA COUPLE OF CHARACTERS 'DB' AT THE BEGINNING AND AT THE END OF THE STRING.
    THE EXTRA CHARACTERS ARE THERE TO HELP WITH THE FORMAT.

    EXAMPLES:
    DECIMAL_TO_BINARY(15)   # RETURNS "DB1111DB"
    DECIMAL_TO_BINARY(32)   # RETURNS "DB100000DB"
    """
    binary = bin(decimal)[2:]  # Convert to binary and remove "0b" prefix
    return "DB" + binary + "DB"