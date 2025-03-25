import math

def rounded_avg(n, m):
    """YOU ARE GIVEN TWO POSITIVE INTEGERS N AND M, AND YOUR TASK IS TO COMPUTE THE
    AVERAGE OF THE INTEGERS FROM N THROUGH M (INCLUDING N AND M). 
    ROUND THE ANSWER TO THE NEAREST INTEGER AND CONVERT THAT TO BINARY.
    IF N IS GREATER THAN M, RETURN -1.
    EXAMPLE:
    ROUNDED_AVG(1, 5) => "0B11"
    ROUNDED_AVG(7, 5) => -1
    ROUNDED_AVG(10, 20) => "0B1111"
    ROUNDED_AVG(20, 33) => "0B11010"
    """
    if n > m:
        return -1
    
    total_sum = sum(range(n, m + 1))
    count = m - n + 1
    average = total_sum / count
    rounded_average = round(average)
    binary_representation = bin(rounded_average)
    return binary_representation