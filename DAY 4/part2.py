# Hints for Part 1 by -> https://www.reddit.com/r/adventofcode/comments/1pdr8x6/comment/ns7iw0y/?context=3&utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
# Slight help from https://github.com/stOneskull/AoC/blob/main/2025/04/paper2.py

# Read the file.
with open("DAY 4\input.txt", "r") as file:
    grid = [list(line.strip()) for line in file.readlines()]

# The grid output is 137x137

# Value of the griddy dimensions.
grid_column = len(grid[0])
grid_row = len(grid)

# Cardinal directions for adjacent elements.
directions = [(-1, -1), (-1, 0), (-1,  1),
              ( 0, -1),          ( 0,  1),
              ( 1, -1), ( 1, 0), ( 1,  1)]

def checkoutofbounds(row, column):

    # Checks if the adjacent hits negative or went too far ahead.
    if (row < 0 or column < 0 or row > len(grid) - 1 or column > len(grid[0]) - 1):
        return 0
    else:
        return 1


# Total count of forkliftable papers
forkliftpapertotal = 0

# The recipe is using these two.
# https://www.geeksforgeeks.org/dsa/introduction-to-matrix-or-grid-data-structure-and-algorithms-tutorial/
# https://www.geeksforgeeks.org/dsa/find-all-adjacent-elements-of-given-element-in-a-2d-array-or-matrix/

# Traverse each element in the grid.

needstochange = True

while needstochange:

    remove = []
    total_changes = 0

    for row in range(grid_row):

        for column in range(len(grid[row])):

            total_adjacent = 0
        
            # Check for only @.
            if(grid[row][column] == '@'):

                for adjacentrow, adjacentcolumn in directions:
                    newrow = row + adjacentrow
                    newcolumn = column + adjacentcolumn

                    if(checkoutofbounds(row + adjacentrow, column + adjacentcolumn)):

                        if(grid[newrow][newcolumn] == '@'):
                            total_adjacent += 1
                            
                if(total_adjacent < 4):
                    forkliftpapertotal += 1
                    total_changes += 1
                    remove.append((newrow, newcolumn))

    for row, column in remove:
        row = row - 1
        column = column - 1

        grid[row][column] = "."
    

    print("You can forklift ", forkliftpapertotal, " papers.")

    if (total_changes == 0):
        needstochange = False


    

            



