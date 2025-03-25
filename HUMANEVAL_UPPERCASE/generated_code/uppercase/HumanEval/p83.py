def starts_one_ends(n):
    """
    GIVEN A POSITIVE INTEGER N, RETURN THE COUNT OF THE NUMBERS OF N-DIGIT
    POSITIVE INTEGERS THAT START OR END WITH 1.
    """
    if n == 1:
        return 1  # Only '1' satisfies the condition

    # Count of n-digit numbers starting with 1: 1 * 10^(n-1)
    starts_with_one = 10**(n-1)

    # Count of n-digit numbers ending with 1: 9 * 10**(n-2) (first digit can't be 0)
    ends_with_one = 10**(n-1)

    # Count of n-digit numbers starting and ending with 1: 1 * 10**(n-2)
    starts_and_ends_with_one = 10**(n-2)

    # Apply the principle of inclusion-exclusion:
    # Count = (starts_with_one) + (ends_with_one) - (starts_and_ends_with_one)
    total_count = starts_with_one + ends_with_one - starts_and_ends_with_one

    return total_count