def cycpattern_check(a , b):
    """YOU ARE GIVEN 2 WORDS. YOU NEED TO RETURN TRUE IF THE SECOND WORD OR ANY OF ITS ROTATIONS IS A SUBSTRING IN THE FIRST WORD
    CYCPATTERN_CHECK("ABCD","ABD") => FALSE
    CYCPATTERN_CHECK("HELLO","ELL") => TRUE
    CYCPATTERN_CHECK("WHASSUP","PSUS") => FALSE
    CYCPATTERN_CHECK("ABAB","BAA") => TRUE
    CYCPATTERN_CHECK("EFEF","EEFF") => FALSE
    CYCPATTERN_CHECK("HIMENSS","SIMEN") => TRUE

    """
    if not b:
        return True
    
    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False