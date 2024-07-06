```markdown
# ALX Interview - Lockboxes

This repository contains a solution to the "Lockboxes" problem. Below is a description of the problem and the solution.

## Problem Description

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- **Prototype:** `def canUnlockAll(boxes)`
- **Parameters:**
  - `boxes` is a list of lists.
- **Constraints:**
  - A key with the same number as a box opens that box.
  - All keys will be positive integers.
  - There can be keys that do not have boxes.
  - The first box `boxes[0]` is unlocked.
- **Returns:** `True` if all boxes can be opened, else `False`.

## Usage

### Example

```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
```

### Output
```sh
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
```

## Repository Structure

```plaintext
.
├── 0-lockboxes.py
├── main_0.py
└── README.md
```

## How to Run

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/alx-interview.git
    cd alx-interview/0x01-lockboxes
    ```

2. Run the main file:
    ```sh
    ./main_0.py
    ```

## Author
Ian Wainaina Kamau
```

