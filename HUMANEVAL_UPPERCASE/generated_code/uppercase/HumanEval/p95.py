def check_dict_case(dict):
    """
    GIVEN A DICTIONARY, RETURN TRUE IF ALL KEYS ARE STRINGS IN LOWER 
    CASE OR ALL KEYS ARE STRINGS IN UPPER CASE, ELSE RETURN FALSE.
    THE FUNCTION SHOULD RETURN FALSE IS THE GIVEN DICTIONARY IS EMPTY.
    EXAMPLES:
    CHECK_DICT_CASE({"A":"APPLE", "B":"BANANA"}) SHOULD RETURN TRUE.
    CHECK_DICT_CASE({"A":"APPLE", "A":"BANANA", "B":"BANANA"}) SHOULD RETURN FALSE.
    CHECK_DICT_CASE({"A":"APPLE", 8:"BANANA", "A":"APPLE"}) SHOULD RETURN FALSE.
    CHECK_DICT_CASE({"NAME":"JOHN", "AGE":"36", "CITY":"HOUSTON"}) SHOULD RETURN FALSE.
    CHECK_DICT_CASE({"STATE":"NC", "ZIP":"12345" }) SHOULD RETURN TRUE.
    """
    if not dict:
        return False

    keys = list(dict.keys())
    if not all(isinstance(key, str) for key in keys):
        return False
    
    first_key = keys[0]
    if first_key.islower():
        return all(key.islower() for key in keys)
    elif first_key.isupper():
        return all(key.isupper() for key in keys)
    else:
        return False