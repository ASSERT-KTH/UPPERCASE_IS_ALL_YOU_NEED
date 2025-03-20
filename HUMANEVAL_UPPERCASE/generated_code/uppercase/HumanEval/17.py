from typing import List


def parse_music(music_string: str) -> List[int]:
    """ INPUT TO THIS FUNCTION IS A STRING REPRESENTING MUSICAL NOTES IN A SPECIAL ASCII FORMAT.
    YOUR TASK IS TO PARSE THIS STRING AND RETURN LIST OF INTEGERS CORRESPONDING TO HOW MANY BEATS DOES EACH
    NOT LAST.

    HERE IS A LEGEND:
    'O' - WHOLE NOTE, LASTS FOUR BEATS
    'O|' - HALF NOTE, LASTS TWO BEATS
    '.|' - QUATER NOTE, LASTS ONE BEAT

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    result = []
    notes = music_string.split()
    for note in notes:
        if note == 'o':
            result.append(4)
        elif note == 'o|':
            result.append(2)
        elif note == '.|':
            result.append(1)
    return result