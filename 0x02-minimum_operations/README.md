# Minimum Operations Project

Welcome to the **Minimum Operations Project**! This project tackles a classic problem in computer science: determining the minimum number of operations needed to achieve a specific goal using a constrained set of actions. Specifically, this project focuses on calculating the fewest number of operations required to generate exactly `n` characters in a text file, starting with a single character 'H' and using only "Copy All" and "Paste" operations.

## Table of Contents

1. [Introduction](#introduction)
2. [Problem Statement](#problem-statement)
3. [Examples](#examples)
4. [Usage](#usage)
5. [Author](#author)

## Introduction

In many text editors, certain operations are fundamental for manipulating text. This project explores the efficiency of these operations by limiting them to "Copy All" and "Paste" actions. The challenge is to determine the minimum number of such operations needed to achieve a desired number of characters.

## Problem Statement

Given a number `n`, write a function `minOperations(n)` that calculates the fewest number of operations needed to result in exactly `n` 'H' characters in the file. The function should return an integer representing the minimum number of operations. If `n` is impossible to achieve, the function should return `0`.

### Function Prototype

```python
def minOperations(n)
```

### Parameters

- `n` (int): The target number of 'H' characters.

### Returns

- `int`: The minimum number of operations needed to reach `n` 'H' characters, or `0` if it's impossible.

## Examples

Consider the following example to better understand the problem:

### Example 1

```python
n = 9

# Sequence of operations:
# H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

# Number of operations: 6
print(minOperations(9)) # Output: 6
```

### Example 2

```python
n = 4
# Sequence of operations:
# H => Copy All => Paste => HH => Copy All => Paste => HHHH

# Number of operations: 4
print(minOperations(4)) # Output: 4
```

### Example 3

```python
n = 12
# Sequence of operations:
# H => Copy All => Paste => HH => Copy All => Paste => HHHH => Copy All => Paste => HHHHHHHHHHHH

# Number of operations: 7
print(minOperations(12)) # Output: 7
```

## Usage

To use the function `minOperations`, simply import it from the module and pass the desired number of characters as an argument. The function will return the minimum number of operations required.

### Example Code

Create a Python file `0-main.py` with the following content to test the function:

```python
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))
```

Run the script:

```bash
$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
```

## Author

This project is authored by Nainah23. If you have any questions or need further assistance, feel free to reach out.

Happy coding!
