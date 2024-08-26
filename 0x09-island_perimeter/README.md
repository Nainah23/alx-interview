---

# 0x09-island_perimeter

This project focuses on calculating the perimeter of an island represented in a 2D grid.

## Task

### 0. Island Perimeter

**Objective:** Implement a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`.

- **Prototype:** `def island_perimeter(grid):`
- **Grid Representation:**
  - `grid` is a list of lists of integers where:
    - `0` represents water.
    - `1` represents land.
  - Each cell in the grid is a square with a side length of 1.
  - Cells are connected horizontally or vertically (not diagonally).
  - The grid is rectangular, with both its width and height not exceeding 100.
- **Assumptions:**
  - The grid is completely surrounded by water.
  - There is only one island or no island at all.
  - The island does not have any lakes (water that is not connected to the water surrounding the island).

### Example Usage

```python
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output: 12
```

## Repository Information

- **GitHub Repository:** `alx-interview`
- **Directory:** `0x09-island_perimeter`
- **File:** `0-island_perimeter.py`

--- 
