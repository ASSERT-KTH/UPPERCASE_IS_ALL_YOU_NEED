def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1

    total_numbers = 9 * (10**(n-1))  # Total n-digit numbers excluding those starting with 0
    starts_with_one = 10**(n-1)  # Numbers starting with 1
    ends_with_one = 10**(n-1)  # Numbers ending with 1 since we allow leading zeros
    starts_and_ends_with_one = 10**(n-2)

    result = starts_with_one + ends_with_one - starts_and_ends_with_one
    return result