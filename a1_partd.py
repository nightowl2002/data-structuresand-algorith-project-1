#    Main Author(s): 
#    Main Reviewer(s):

# a1_partd.py

def get_overflow_list(grid):
    rows, cols = len(grid), len(grid[0])
    overflow_list = []

    for i in range(rows):
        for j in range(cols):
            neighbors = [
                (i-1, j), (i+1, j), (i, j-1), (i, j+1)
            ]

            neighbor_count = sum(1 for x, y in neighbors if 0 <= x < rows and 0 <= y < cols)

            if grid[i][j] >= neighbor_count:
                overflow_list.append((i, j))

    return overflow_list


def overflow(grid, a_queue):
    def is_valid_cell(x, y):
        return 0 <= x < rows and 0 <= y < cols

    rows, cols = len(grid), len(grid[0])
    overflow_list = get_overflow_list(grid)

    if not overflow_list:
        return 0  # No overflowing cells

    # Check if signs of non-zero cells are the same
    signs = set(grid[i][j] for i in range(rows) for j in range(cols) if grid[i][j] != 0)
    if len(signs) == 1:
        return 0  # Signs are the same, no need to overflow

    new_grid = [row.copy() for row in grid]

    for i, j in overflow_list:
        overflow_value = grid[i][j]
        new_grid[i][j] = 0  # Empty the overflowing cell

        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if is_valid_cell(x, y):
                new_grid[x][y] += 1  # Add one extra item to the neighbor
                if grid[x][y] == 0:
                    new_grid[x][y] = overflow_value // abs(overflow_value)

    a_queue.enqueue(new_grid)
    return 1 + overflow(new_grid, a_queue)



