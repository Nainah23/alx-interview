# 0x04-utf8_validation

## Description
This project involves creating a function to determine if a given data set represents a valid UTF-8 encoding. UTF-8 is a variable-width character encoding used for electronic communication, and it can encode all possible characters (code points) in Unicode using one to four one-byte (8-bit) units.

## Files

- `0-validate_utf8.py`: Contains the `validUTF8` function.
- `0-main.py`: Main file for testing the `validUTF8` function.

## Requirements
- Python 3.x
- The function must be named `validUTF8`.
- The function must return `True` if the data set represents a valid UTF-8 encoding, and `False` otherwise.
- A character in UTF-8 can be 1 to 4 bytes long.
- The data set can contain multiple characters.
- The data will be represented by a list of integers.
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer.

## Usage

### Prototype
```python
def validUTF8(data)
```

### Example
```python
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
```

### Running the Example
To run the example, save the code above in a file named `0-main.py`, ensure that `0-validate_utf8.py` is in the same directory, and execute the following command in your terminal:
```bash
./0-main.py
```

## Repository Structure
```
.
├── 0-main.py
└── 0-validate_utf8.py
```

## Testing
The provided `0-main.py` file contains tests for the `validUTF8` function. You can add more test cases to ensure the function handles various scenarios and edge cases correctly.

## License
