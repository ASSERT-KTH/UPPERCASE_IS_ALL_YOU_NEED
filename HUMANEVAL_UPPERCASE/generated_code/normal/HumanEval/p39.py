def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    fib_numbers = [0, 1]
    while True:
        next_fib = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(next_fib)
        
        prime_fib_numbers = []
        for fib_num in fib_numbers:
            if is_prime(fib_num):
                prime_fib_numbers.append(fib_num)
        
        if len(prime_fib_numbers) >= n:
            return prime_fib_numbers[n-1]