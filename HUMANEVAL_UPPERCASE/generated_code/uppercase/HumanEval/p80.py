def is_happy(s):
    """YOU ARE GIVEN A STRING S.
    YOUR TASK IS TO CHECK IF THE STRING IS HAPPY OR NOT.
    A STRING IS HAPPY IF ITS LENGTH IS AT LEAST 3 AND EVERY 3 CONSECUTIVE LETTERS ARE DISTINCT
    FOR EXAMPLE:
    IS_HAPPY(A) => FALSE
    IS_HAPPY(AA) => FALSE
    IS_HAPPY(ABCD) => TRUE
    IS_HAPPY(AABB) => FALSE
    IS_HAPPY(ADB) => TRUE
    IS_HAPPY(XYY) => FALSE
    """
    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2] :
            return False

    return True