def get_row(lst, x):
    """
    YOU ARE GIVEN A 2 DIMENSIONAL DATA, AS A NESTED LISTS,
    WHICH IS SIMILAR TO MATRIX, HOWEVER, UNLIKE MATRICES,
    EACH ROW MAY CONTAIN A DIFFERENT NUMBER OF COLUMNS.
    GIVEN LST, AND INTEGER X, FIND INTEGERS X IN THE LIST,
    AND RETURN LIST OF TUPLES, [(X1, Y1), (X2, Y2) ...] SUCH THAT
    EACH TUPLE IS A COORDINATE - (ROW, COLUMNS), STARTING WITH 0.
    SORT COORDINATES INITIALLY BY ROWS IN ASCENDING ORDER.
    ALSO, SORT COORDINATES OF THE ROW BY COLUMNS IN DESCENDING ORDER.
    
    EXAMPLES:
    GET_ROW([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    GET_ROW([], 1) == []
    GET_ROW([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    coordinates = []
    for r, row in enumerate(lst):
        for c, val in enumerate(row):
            if val == x:
                coordinates.append((r, c))
    
    coordinates.sort(key=lambda coord: (coord[0])) #Sort by row (ascending)
    
    
    
    sorted_coordinates = []
    row_groups = {}
    for r,c in coordinates:
        if r not in row_groups:
            row_groups[r] = []
        row_groups[r].append(c)
    
    for r in sorted(row_groups.keys()):
        row_groups[r].sort(reverse=True)
        for c in row_groups[r]:
            sorted_coordinates.append((r,c))
    
    return sorted_coordinates