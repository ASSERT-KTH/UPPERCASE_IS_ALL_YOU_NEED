def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    if not array:
        return []

    arr_copy = array[:]  # Create a copy to avoid modifying the original

    if len(array) > 1:
      first_index_value = array[0]
      last_index_value = array[-1]
      sum_of_values = first_index_value + last_index_value

      if sum_of_values % 2 != 0:  # Odd sum, sort in ascending order
          arr_copy.sort()
      else:  # Even sum, sort in descending order
          arr_copy.sort(reverse=True)

    return arr_copy