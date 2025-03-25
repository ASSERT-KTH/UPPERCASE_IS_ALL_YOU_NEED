def sort_array(array):
    """
    GIVEN AN ARRAY OF NON-NEGATIVE INTEGERS, RETURN A COPY OF THE GIVEN ARRAY AFTER SORTING,
    YOU WILL SORT THE GIVEN ARRAY IN ASCENDING ORDER IF THE SUM( FIRST INDEX VALUE, LAST INDEX VALUE) IS ODD,
    OR SORT IT IN DESCENDING ORDER IF THE SUM( FIRST INDEX VALUE, LAST INDEX VALUE) IS EVEN.

    NOTE:
    * DON'T CHANGE THE GIVEN ARRAY.

    EXAMPLES:
    * SORT_ARRAY([]) => []
    * SORT_ARRAY([5]) => [5]
    * SORT_ARRAY([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * SORT_ARRAY([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    if not array:
        return []

    new_array = array[:]  # Create a copy to avoid modifying the original

    if len(array) == 1:
        return new_array

    first_element = array[0]
    last_element = array[-1]
    sum_of_elements = first_element + last_element

    if sum_of_elements % 2 != 0:  # Odd sum, sort in ascending order
        new_array.sort()
    else:  # Even sum, sort in descending order
        new_array.sort(reverse=True)

    return new_array