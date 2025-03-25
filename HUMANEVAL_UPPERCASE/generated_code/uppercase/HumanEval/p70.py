def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    if not lst:
        return []

    sorted_lst = []
    nums = sorted(lst)
    left, right = 0, len(nums) - 1
    turn = 0  # 0 for min, 1 for max
    while left <= right:
        if turn == 0:
            sorted_lst.append(nums[left])
            left += 1
        else:
            sorted_lst.append(nums[right])
            right -= 1
        turn = 1 - turn
    return sorted_lst