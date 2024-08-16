---

# 0x07 - Rotate 2D Matrix

This project involves rotating a given `n x n` 2D matrix by 90 degrees clockwise. The goal is to modify the matrix in place without using any additional memory for another matrix.

## Task

### Rotate 2D Matrix

Given an `n x n` 2D matrix, rotate it 90 degrees clockwise.

### Prototype

```python
def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix by 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): The n x n 2D matrix to be rotated.

    Returns:
        None
    """
```

### Requirements

- The function should not return anything. The matrix must be edited in-place.
- You can assume that the matrix will have 2 dimensions and will not be empty.

### Example

Given the following matrix:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

After calling `rotate_2d_matrix(matrix)`, the matrix should be updated to:

```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

### Usage

To test the function, you can use the following script:

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
```

When you run the script, the output should be:

```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Repository

- **GitHub Repository:** [alx-interview](https://github.com/Nainah23/alx-interview)
- **Directory:** `0x07-rotate_2d_matrix`
- **File:** `0-rotate_2d_matrix.py`

## Author

This project was created as part of the ALX Software Engineering program.

--- 
