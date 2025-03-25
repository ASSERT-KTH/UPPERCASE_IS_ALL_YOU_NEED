def max_fill(grid, capacity):
    import math
    """
    YOU ARE GIVEN A RECTANGULAR GRID OF WELLS. EACH ROW REPRESENTS A SINGLE WELL,
    AND EACH 1 IN A ROW REPRESENTS A SINGLE UNIT OF WATER.
    EACH WELL HAS A CORRESPONDING BUCKET THAT CAN BE USED TO EXTRACT WATER FROM IT, 
    AND ALL BUCKETS HAVE THE SAME CAPACITY.
    YOUR TASK IS TO USE THE BUCKETS TO EMPTY THE WELLS.
    OUTPUT THE NUMBER OF TIMES YOU NEED TO LOWER THE BUCKETS.

    EXAMPLE 1:
        INPUT: 
            GRID : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            BUCKET_CAPACITY : 1
        OUTPUT: 6

    EXAMPLE 2:
        INPUT: 
            GRID : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            BUCKET_CAPACITY : 2
        OUTPUT: 5
    
    EXAMPLE 3:
        INPUT: 
            GRID : [[0,0,0], [0,0,0]]
            BUCKET_CAPACITY : 5
        OUTPUT: 0

    CONSTRAINTS:
        * ALL WELLS HAVE THE SAME LENGTH
        * 1 <= GRID.LENGTH <= 10^2
        * 1 <= GRID[:,1].LENGTH <= 10^2
        * GRID[I][J] -> 0 | 1
        * 1 <= CAPACITY <= 10
    """
    count = 0
    for row in grid:
        water_units = sum(row)
        if water_units > 0:
            count += math.ceil(water_units / capacity)
    return count