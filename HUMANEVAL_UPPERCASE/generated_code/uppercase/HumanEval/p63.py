def fibfib(n: int):
    """THE FIBFIB NUMBER SEQUENCE IS A SEQUENCE SIMILAR TO THE FIBBONACCI SEQUNECE THAT'S DEFINED AS FOLLOWS:
    FIBFIB(0) == 0
    FIBFIB(1) == 0
    FIBFIB(2) == 1
    FIBFIB(N) == FIBFIB(N-1) + FIBFIB(N-2) + FIBFIB(N-3).
    PLEASE WRITE A FUNCTION TO EFFICIENTLY COMPUTE THE N-TH ELEMENT OF THE FIBFIB NUMBER SEQUENCE.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n <= 1:
        return 0
    if n == 2:
        return 1
    
    fib_seq = [0, 0, 1]
    for i in range(3, n + 1):
        next_fib = fib_seq[i-1] + fib_seq[i-2] + fib_seq[i-3]
        fib_seq.append(next_fib)
    
    return fib_seq[n]