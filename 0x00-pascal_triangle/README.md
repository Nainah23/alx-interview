```markdown
# Pascal's Triangle

This project contains a function to generate Pascal's Triangle, a triangular array of binomial coefficients.

## Description

The function `pascal_triangle(n)` generates the first `n` rows of Pascal's Triangle. Pascal's Triangle is a triangular array where each number is the sum of the two numbers directly above it in the previous row.

## Usage

### Function Definition

```python
def pascal_triangle(n):
    # Function implementation
```

- **Parameters**: 
  - `n` (int): The number of rows of Pascal's Triangle to generate.
- **Returns**: 
  - A list of lists of integers representing Pascal's Triangle. If `n` <= 0, it returns an empty list.

### Example

```python
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$
```

## Example Output

For `n = 5`, the output will be:
```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

## Repository

- **GitHub repository**: [alx-interview](https://github.com/your-username/alx-interview)
- **Directory**: `0x00-pascal_triangle`
- **File**: `0-pascal_triangle.py`

Feel free to clone this repository and experiment with the function. Contributions and improvements are welcome!
```