def prime_fib(n: int):
    """
    PRIME_FIB RETURNS N-TH NUMBER THAT IS A FIBONACCI NUMBER AND IT'S ALSO PRIME.
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
    prime_fib_numbers = []
    i = 2
    while len(prime_fib_numbers) < n:
        next_fib = fib_numbers[i - 1] + fib_numbers[i - 2]
        fib_numbers.append(next_fib)
        if is_prime(next_fib):
            prime_fib_numbers.append(next_fib)
        i += 1

    return prime_fib_numbers[n - 1]