def fix_spaces(text):
    """
    GIVEN A STRING TEXT, REPLACE ALL SPACES IN IT WITH UNDERSCORES, 
    AND IF A STRING HAS MORE THAN 2 CONSECUTIVE SPACES, 
    THEN REPLACE ALL CONSECUTIVE SPACES WITH - 
    
    FIX_SPACES("EXAMPLE") == "EXAMPLE"
    FIX_SPACES("EXAMPLE 1") == "EXAMPLE_1"
    FIX_SPACES(" EXAMPLE 2") == "_EXAMPLE_2"
    FIX_SPACES(" EXAMPLE   3") == "_EXAMPLE-3"
    """
    
    new_text = text.replace(" ", "_")
    
    while "--" in new_text:
        new_text = new_text.replace("--", "-")
    
    return new_text