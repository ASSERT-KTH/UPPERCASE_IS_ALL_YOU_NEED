def specialFilter(nums):
    """WRITE A FUNCTION THAT TAKES AN ARRAY OF NUMBERS AS INPUT AND RETURNS 
    THE NUMBER OF ELEMENTS IN THE ARRAY THAT ARE GREATER THAN 10 AND BOTH 
    FIRST AND LAST DIGITS OF A NUMBER ARE ODD (1, 3, 5, 7, 9).
    FOR EXAMPLE:
    SPECIALFILTER([15, -73, 14, -15]) => 1 
    SPECIALFILTER([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))  # Handle negative numbers
            if len(num_str) > 0: # Handle the case where the number might be zero
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])

                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count