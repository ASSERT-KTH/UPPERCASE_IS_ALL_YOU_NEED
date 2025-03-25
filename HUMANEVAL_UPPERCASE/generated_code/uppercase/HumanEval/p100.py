def make_a_pile(n):
    """
    GIVEN A POSITIVE INTEGER N, YOU HAVE TO MAKE A PILE OF N LEVELS OF STONES.
    THE FIRST LEVEL HAS N STONES.
    THE NUMBER OF STONES IN THE NEXT LEVEL IS:
        - THE NEXT ODD NUMBER IF N IS ODD.
        - THE NEXT EVEN NUMBER IF N IS EVEN.
    RETURN THE NUMBER OF STONES IN EACH LEVEL IN A LIST, WHERE ELEMENT AT INDEX
    I REPRESENTS THE NUMBER OF STONES IN THE LEVEL (I+1).

    EXAMPLES:
    >>> make_a_pile(3)
    [3, 5, 7]
    """

    pile = []
    for _ in range(n):
        pile.append(n)
        if n % 2 == 0:
            n += 2
        else:
            n += 2
    return pile