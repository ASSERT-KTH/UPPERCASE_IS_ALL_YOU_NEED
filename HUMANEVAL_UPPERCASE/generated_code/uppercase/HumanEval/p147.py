def get_max_triples(n):
    """
    YOU ARE GIVEN A POSITIVE INTEGER N. YOU HAVE TO CREATE AN INTEGER ARRAY A OF LENGTH N.
        FOR EACH I (1 ≤ I ≤ N), THE VALUE OF A[I] = I * I - I + 1.
        RETURN THE NUMBER OF TRIPLES (A[I], A[J], A[K]) OF A WHERE I < J < K, 
    AND A[I] + A[J] + A[K] IS A MULTIPLE OF 3.

    EXAMPLE :
        INPUT: N = 5
        OUTPUT: 1
        EXPLANATION: 
        A = [1, 3, 7, 13, 21]
        THE ONLY VALID TRIPLE IS (1, 7, 13).
    """
    a = []
    for i in range(1, n + 1):
        a.append(i * i - i + 1)
    
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count