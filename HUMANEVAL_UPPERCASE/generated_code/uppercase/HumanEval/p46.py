def fib4(n: int):
    """THE FIB4 NUMBER SEQUENCE IS A SEQUENCE SIMILAR TO THE FIBBONACCI SEQUNECE THAT'S DEFINED AS FOLLOWS:
    FIB4(0) -> 0
    FIB4(1) -> 0
    FIB4(2) -> 2
    FIB4(3) -> 0
    FIB4(N) -> FIB4(N-1) + FIB4(N-2) + FIB4(N-3) + FIB4(N-4).
    PLEASE WRITE A FUNCTION TO EFFICIENTLY COMPUTE THE N-TH ELEMENT OF THE FIB4 NUMBER SEQUENCE.  DO NOT USE RECURSION.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    fib_values = [0, 0, 2, 0]  # Initialize with the first four values

    for i in range(4, n + 1):
        next_fib = fib_values[0] + fib_values[1] + fib_values[2] + fib_values[3]
        fib_values.pop(0)  # Remove the oldest value
        fib_values.append(next_fib)  # Add the new value

    return fib_values[-1]