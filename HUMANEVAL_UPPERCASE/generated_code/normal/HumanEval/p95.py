def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if not dict:
        return False

    keys = list(dict.keys())
    if not all(isinstance(key, str) for key in keys):
        return False

    first_key = keys[0]

    if first_key.islower():
        for key in keys:
            if not key.islower():
                return False
        return True
    elif first_key.isupper():
        for key in keys:
            if not key.isupper():
                return False
        return True
    else:
        return False