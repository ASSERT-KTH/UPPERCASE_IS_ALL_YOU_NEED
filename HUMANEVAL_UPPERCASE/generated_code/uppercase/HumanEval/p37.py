def sort_even(l: list):
    """THIS FUNCTION TAKES A LIST L AND RETURNS A LIST L' SUCH THAT
    L' IS IDENTICAL TO L IN THE ODD INDICIES, WHILE ITS VALUES AT THE EVEN INDICIES ARE EQUAL
    TO THE VALUES OF THE EVEN INDICIES OF L, BUT SORTED.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indices = []
    for i in range(len(l)):
        if i % 2 == 0:
            even_indices.append(l[i])
    even_indices.sort()
    l_prime = []
    even_index_counter = 0
    for i in range(len(l)):
        if i % 2 == 0:
            l_prime.append(even_indices[even_index_counter])
            even_index_counter += 1
        else:
            l_prime.append(l[i])
    return l_prime