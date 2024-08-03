---

# N Queens Problem

The N Queens problem is a classic challenge in combinatorial optimization and backtracking algorithms. The goal is to place N non-attacking queens on an N×N chessboard such that no two queens threaten each other.

## Project Overview

This project provides a Python script to solve the N Queens problem. The script generates all possible solutions for placing N queens on an N×N chessboard where no two queens can attack each other.

## Requirements

- Python 3.x
- Only the `sys` module is allowed for imports.

## Usage

To run the script and solve the N Queens problem, use the following command:

```bash
./0-nqueens.py N
```

Replace `N` with the integer representing the size of the chessboard and the number of queens to place.

### Validations

- If the number of arguments is incorrect, the script will print:
  ```
  Usage: nqueens N
  ```
  and exit with status 1.

- If `N` is not an integer, the script will print:
  ```
  N must be a number
  ```
  and exit with status 1.

- If `N` is smaller than 4, the script will print:
  ```
  N must be at least 4
  ```
  and exit with status 1.

## Example

### Example 1: 

```bash
./0-nqueens.py 4
```

Output:

```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

### Example 2:

```bash
./0-nqueens.py 6
```

Output:

```
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Files

- `0-nqueens.py`: Python script that solves the N Queens problem.

## Repository

- GitHub repository: [alx-interview](https://github.com/yourusername/alx-interview)
- Directory: `0x05-nqueens`

---
