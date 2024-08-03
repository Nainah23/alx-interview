#!/usr/bin/python3
"""
    Description: The N Queens puzzle involves placing N non-attacking queens
                 on an N×N chessboard. This script solves the N Queens problem
                 by finding all possible solutions.
    Usage: nqueens N
           If the program is called with an incorrect number of arguments,
           it will print Usage: nqueens N, followed by a new line, and exit
           with status 1.
           N must be an integer that is 4 or greater:
           If N is not an integer, the script will print N must be a number,
           followed by a new line, and exit with status 1.
           If N is less than 4, it will print N must be at least 4, followed by
           a new line, and exit with status 1.
    The script will output all possible solutions to the problem:
           Each solution will be printed on a separate line.
           The solutions do not need to be in any specific order.
    Only the sys module is permitted for import.
"""

import sys


def print_board(board):
    """ print_board
    Args:
        board - list of list with length sys.argv[1]
    """
    new_list = []
    for i, row in enumerate(board):
        value = []
        for j, col in enumerate(row):
            if col == 1:
                value.append(i)
                value.append(j)
        new_list.append(value)

    print(new_list)


def isSafe(board, row, col, number):
    """ isSafe
    Args:
        board - list of list with length sys.argv[1]
        row - row to check if is safe doing a movement in this position
        col - col to check if is safe doing a movement in this position
        number: size of the board
    Return: True of False
    """

    # Check this row in the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, number, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col, number):
    """ Auxiliary method to find the solutions
    Args:
        board - Board to solve
        col - Number of column
        number - size of the board
    Returns:
        All possible solutions to the problem
    """

    if col == number:
        print_board(board)
        return True
    res = False
    for i in range(number):

        if isSafe(board, i, col, number):

            # Place this queen in board[i][col]
            board[i][col] = 1

            # Make result true if any placement
            # is possible
            res = solveNQUtil(board, col + 1, number) or res

            board[i][col] = 0  # BACKTRACK

    return res


def solve(number):
    """ Find all possible solutions
    Args:
        number - size of the board
    """
    board = [[0 for _ in range(number)] for _ in range(number)]

    if not solveNQUtil(board, 0, number):
        return False

    return True


def validate(args):
    """ Validate the input data
    Args:
        args - sys.argv
    """
    if len(args) == 2:
        # Validate data
        try:
            number = int(args[1])
        except Exception:
            print("N must be a number")
            exit(1)
        if number < 4:
            print("N must be at least 4")
            exit(1)
        return number
    else:
        print("Usage: nqueens N")
        exit(1)


if __name__ == "__main__":
    """ Main method to execute the script
    """
    number = validate(sys.argv)
    solve(number)
