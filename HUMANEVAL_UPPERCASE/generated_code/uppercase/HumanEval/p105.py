def by_length(arr):
    """
    GIVEN AN ARRAY OF INTEGERS, SORT THE INTEGERS THAT ARE BETWEEN 1 AND 9 INCLUSIVE,
    REVERSE THE RESULTING ARRAY, AND THEN REPLACE EACH DIGIT BY ITS CORRESPONDING NAME FROM
    "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE".

    FOR EXAMPLE:
      ARR = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> SORT ARR -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> REVERSE ARR -> [8, 5, 4, 3, 2, 2, 1, 1]
      RETURN ["EIGHT", "FIVE", "FOUR", "THREE", "TWO", "TWO", "ONE", "ONE"]
    
      IF THE ARRAY IS EMPTY, RETURN AN EMPTY ARRAY:
      ARR = []
      RETURN []
    
      IF THE ARRAY HAS ANY STRANGE NUMBER IGNORE IT:
      ARR = [1, -1 , 55] 
            -> SORT ARR -> [-1, 1, 55]
            -> REVERSE ARR -> [55, 1, -1]
      RETURN = ['ONE']
    """
    if not arr:
        return []

    # Filter and sort the numbers between 1 and 9
    filtered_arr = sorted([num for num in arr if 1 <= num <= 9])

    # Reverse the sorted array
    reversed_arr = filtered_arr[::-1]

    # Map digits to their corresponding names
    digit_names = {
        1: "ONE",
        2: "TWO",
        3: "THREE",
        4: "FOUR",
        5: "FIVE",
        6: "SIX",
        7: "SEVEN",
        8: "EIGHT",
        9: "NINE",
    }

    # Replace digits with names
    result = [digit_names[digit] for digit in reversed_arr]

    return result