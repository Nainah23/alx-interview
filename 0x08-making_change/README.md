---

# 0x08-making_change

This project focuses on solving the "Making Change" problem, where given a pile of coins of different values, the goal is to determine the fewest number of coins needed to meet a given amount.

## Task

### 0. Change Comes From Within

**Objective:** Write a function `makeChange(coins, total)` that determines the fewest number of coins needed to meet a given amount `total`.

- **Prototype:** `def makeChange(coins, total):`
- **Return Value:**
  - Returns the fewest number of coins needed to meet `total`.
  - Returns `0` if `total` is `0` or less.
  - Returns `-1` if `total` cannot be met by any combination of the coins in your possession.
- **Constraints:**
  - `coins` is a list of integers representing the values of the coins.
  - The value of each coin is an integer greater than `0`.
  - You have an infinite number of each denomination of coin in the list.
- **Performance:** The runtime of the solution will be evaluated.

### Example Usage

```python
makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

## Repository Information

- **GitHub Repository:** `alx-interview`
- **Directory:** `0x08-making_change`
- **File:** `0-making_change.py`

--- 
