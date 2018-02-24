# Exercise 1 two ways:
def initialize_robot(grid_size):
    grid = [1/grid_size] * grid_size
    return grid

def initialize_robot(grid_size):

    grid = []

    for i in range(grid_size):
        grid.append(1/grid_size)

    return grid

# Exercise 2
def grid_probability(grid, position):

    if position < len(grid):
        return grid[position]

    return None

# Exercise 3
import matplotlib.pyplot as plt
import numpy as np

def output_map(grid):

    x_labels = range(len(grid))

    plt.bar(x_labels, grid)
    plt.xlabel('Grid Space')
    plt.ylabel('Probability')
    plt.title('Probability of the Robot Being at Each Space on the Grid')
    plt.show()

# Exercise 4  two ways
def update_probabilities(grid, updates):

    for i in range(len(updates)):
        grid[updates[i][0]] = updates[i][1]

    return grid

def update_probabilities(grid, updates):
    for update in updates:
        grid[update[0]] = update[1]
    return grid
