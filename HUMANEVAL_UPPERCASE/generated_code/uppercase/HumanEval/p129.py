from collections import deque

def minPath(grid, k):
    """
    GIVEN A GRID WITH N ROWS AND N COLUMNS (N >= 2) AND A POSITIVE INTEGER K, 
    EACH CELL OF THE GRID CONTAINS A VALUE. EVERY INTEGER IN THE RANGE [1, N * N]
    INCLUSIVE APPEARS EXACTLY ONCE ON THE CELLS OF THE GRID.

    YOU HAVE TO FIND THE MINIMUM PATH OF LENGTH K IN THE GRID. YOU CAN START
    FROM ANY CELL, AND IN EACH STEP YOU CAN MOVE TO ANY OF THE NEIGHBOR CELLS,
    IN OTHER WORDS, YOU CAN GO TO CELLS WHICH SHARE AN EDGE WITH YOU CURRENT
    CELL.
    PLEASE NOTE THAT A PATH OF LENGTH K MEANS VISITING EXACTLY K CELLS (NOT
    NECESSARILY DISTINCT).
    YOU CANNOT GO OFF THE GRID.
    A PATH A (OF LENGTH K) IS CONSIDERED LESS THAN A PATH B (OF LENGTH K) IF
    AFTER MAKING THE ORDERED LISTS OF THE VALUES ON THE CELLS THAT A AND B GO
    THROUGH (LET'S CALL THEM LST_A AND LST_B), LST_A IS LEXICOGRAPHICALLY LESS
    THAN LST_B, IN OTHER WORDS, THERE EXIST AN INTEGER INDEX I (1 <= I <= K)
    SUCH THAT LST_A[I] < LST_B[I] AND FOR ANY J (1 <= J < I) WE HAVE
    LST_A[J] = LST_B[J].
    IT IS GUARANTEED THAT THE ANSWER IS UNIQUE.
    RETURN AN ORDERED LIST OF THE VALUES ON THE CELLS THAT THE MINIMUM PATH GO THROUGH.

    EXAMPLES:

        INPUT: GRID = [ [1,2,3], [4,5,6], [7,8,9]], K = 3
        OUTPUT: [1, 2, 1]

        INPUT: GRID = [ [5,9,3], [4,1,6], [7,8,2]], K = 1
        OUTPUT: [1]
    """
    n = len(grid)
    min_path = None

    for start_row in range(n):
        for start_col in range(n):
            q = deque([([(start_row, start_col)], [grid[start_row][start_col]])])
            
            while q:
                path_coords, path_values = q.popleft()
                
                if len(path_values) == k:
                    if min_path is None or path_values < min_path:
                        min_path = path_values
                    continue

                row, col = path_coords[-1]
                neighbors = []
                if row > 0:
                    neighbors.append((row - 1, col))
                if row < n - 1:
                    neighbors.append((row + 1, col))
                if col > 0:
                    neighbors.append((row, col - 1))
                if col < n - 1:
                    neighbors.append((row, col + 1))
                
                for neighbor_row, neighbor_col in neighbors:
                    new_path_coords = path_coords + [(neighbor_row, neighbor_col)]
                    new_path_values = path_values + [grid[neighbor_row][neighbor_col]]
                    q.append((new_path_coords,new_path_values))
                    
    return min_path