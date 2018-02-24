# Exercise 1
def initial_grid(rows, columns):

    grid = []
    row = []
    probability = 1 / (rows * columns)

    for i in range(rows):
        for j in range(columns):
            row.append(probability)
        grid.append(row)
        row = []

    return grid

# Exercise 2
def probability(grid, row, column):

    return grid[row][column]

# Exercise 3
def update_probability(grid, update_list):
    for element in update_list:
        x, y = element[0]
        grid[x][y] = element[1]

    return grid
