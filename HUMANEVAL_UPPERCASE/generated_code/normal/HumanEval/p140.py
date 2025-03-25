def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    # Replace all spaces with underscores
    text = text.replace(" ", "_")
    
    # Replace consecutive underscores (more than 2) with hyphens
    while "__-" in text:
        text = text.replace("__-", "-")

    
    while "___" in text:
        text = text.replace("___", "--")

    #Replace multiple '_' with '-'
    while "__" in text and "-" not in text:
        text = text.replace("__", "-")
    
    # if text.find("_-") != -1:
    #     text = text.replace("_-", "-_")

    return text