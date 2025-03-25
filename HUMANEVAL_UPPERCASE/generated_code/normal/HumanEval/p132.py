def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if not stack:
                return False
            stack.pop()
    
    if not stack :
        
        stack = []
        nested_found = False
        for char in string:
            if char == '[':
                stack.append(char)
            elif char == ']':
                if len(stack) > 1:
                    nested_found = True
                if not stack:
                    return False
                stack.pop()
                
        return nested_found
    else:
        return False