def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_so_far = float('inf')
    current_min = 0
    for num in nums:
        current_min += num
        min_so_far = min(min_so_far, current_min)
        if current_min > 0:
            current_min = 0
    return min_so_far