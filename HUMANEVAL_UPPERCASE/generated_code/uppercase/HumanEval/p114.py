def minSubArraySum(nums):
    """
    GIVEN AN ARRAY OF INTEGERS NUMS, FIND THE MINIMUM SUM OF ANY NON-EMPTY SUB-ARRAY
    OF NUMS.
    EXAMPLE
    MINSUBARRAYSUM([2, 3, 4, 1, 2, 4]) == 1
    MINSUBARRAYSUM([-1, -2, -3]) == -6
    """
    min_so_far = float('inf')
    current_min = 0
    for i in range(len(nums)):
        current_min += nums[i]
        min_so_far = min(min_so_far, current_min)
        if current_min > 0:
            current_min = 0
    return min_so_far