def Strongest_Extension(class_name, extensions):
    """YOU WILL BE GIVEN THE NAME OF A CLASS (A STRING) AND A LIST OF EXTENSIONS.
    THE EXTENSIONS ARE TO BE USED TO LOAD ADDITIONAL CLASSES TO THE CLASS. THE
    STRENGTH OF THE EXTENSION IS AS FOLLOWS: LET CAP BE THE NUMBER OF THE UPPERCASE
    LETTERS IN THE EXTENSION'S NAME, AND LET SM BE THE NUMBER OF LOWERCASE LETTERS 
    IN THE EXTENSION'S NAME, THE STRENGTH IS GIVEN BY THE FRACTION CAP - SM. 
    YOU SHOULD FIND THE STRONGEST EXTENSION AND RETURN A STRING IN THIS 
    FORMAT: CLASSNAME.STRONGESTEXTENSIONNAME.
    IF THERE ARE TWO OR MORE EXTENSIONS WITH THE SAME STRENGTH, YOU SHOULD
    CHOOSE THE ONE THAT COMES FIRST IN THE LIST.
    FOR EXAMPLE, IF YOU ARE GIVEN "SLICES" AS THE CLASS AND A LIST OF THE
    EXTENSIONS: ['SERVINGSLICES', 'CHEESE', 'STUFFED'] THEN YOU SHOULD
    RETURN 'SLICES.SERVINGSLICES' SINCE 'SERVINGSLICES' IS THE STRONGEST EXTENSION 
    (ITS STRENGTH IS -1).
    EXAMPLE:
    FOR STRONGEST_EXTENSION('MY_CLASS', ['AA', 'BE', 'CC']) == 'MY_CLASS.AA'
    """

    best_extension = ""
    max_strength = float('-inf')

    for extension in extensions:
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm

        if strength > max_strength:
            max_strength = strength
            best_extension = extension

    if best_extension:
        return f"{class_name}.{best_extension}"
    else:
        return class_name