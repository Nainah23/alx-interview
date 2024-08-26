#!/usr/bin/python3
"""
Module that provides a function to calculate the perimeter of an island 
described in a 2D grid.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island described by the grid.

    Args:
        grid (list of list of ints): A 2D grid where 0 represents water and
                                     1 represents land. The grid is rectangular
                                     and cells are connected horizontally/vertically.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    grid_length = len(grid)
    for row in range(grid_length):
        for column in range(len(grid[row])):
            if grid[row][column] == 1:
                if row - 1 < 0 or grid[row - 1][column] == 0:
                    perimeter += 1
                if column - 1 < 0 or grid[row][column - 1] == 0:
                    perimeter += 1
                if column + 1 >= len(grid[row]) or grid[row][column + 1] == 0:
                    perimeter += 1
                if row + 1 >= grid_length or grid[row + 1][column] == 0:
                    perimeter += 1
    return perimeter

