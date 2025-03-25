def do_algebra(operator, operand):
    """
    GIVEN TWO LISTS OPERATOR, AND OPERAND. THE FIRST LIST HAS BASIC ALGEBRA OPERATIONS, AND 
    THE SECOND LIST IS A LIST OF INTEGERS. USE THE TWO GIVEN LISTS TO BUILD THE ALGEBRIC 
    EXPRESSION AND RETURN THE EVALUATION OF THIS EXPRESSION.

    THE BASIC ALGEBRA OPERATIONS:
    ADDITION ( + ) 
    SUBTRACTION ( - ) 
    MULTIPLICATION ( * ) 
    FLOOR DIVISION ( // ) 
    EXPONENTIATION ( ** ) 

    EXAMPLE:
    OPERATOR['+', '*', '-']
    ARRAY = [2, 3, 4, 5]
    RESULT = 2 + 3 * 4 - 5
    => RESULT = 9

    NOTE:
        THE LENGTH OF OPERATOR LIST IS EQUAL TO THE LENGTH OF OPERAND LIST MINUS ONE.
        OPERAND IS A LIST OF OF NON-NEGATIVE INTEGERS.
        OPERATOR LIST HAS AT LEAST ONE OPERATOR, AND OPERAND LIST HAS AT LEAST TWO OPERANDS.

    """
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result