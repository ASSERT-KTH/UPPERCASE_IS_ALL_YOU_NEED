def solution(lst):
    """GIVEN A NON-EMPTY LIST OF INTEGERS, RETURN THE SUM OF ALL OF THE ODD ELEMENTS THAT ARE IN EVEN POSITIONS.
    

    EXAMPLES
    SOLUTION([5, 8, 7, 1]) ==> 12
    SOLUTION([3, 3, 3, 3, 3]) ==> 9
    SOLUTION([30, 13, 24, 321]) ==>0
    """
    sum_of_odds = 0
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            sum_of_odds += lst[i]
    return sum_of_odds