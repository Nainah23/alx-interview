# ALX Interview - Log Parsing

## Project Overview

This project involves writing a script to parse log data, compute metrics, and handle interruptions. The script reads log entries from stdin, processes them to calculate file sizes and status code counts, and displays statistics every 10 lines or upon a keyboard interruption.

## Task Description

### Log Parsing Script

- **Objective**: Write a script (`0-stats.py`) that processes log entries and calculates metrics.
- **Input Format**: The log entries have the following format:
  ```
  <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
  ```
  The script should:
  - Read and parse log entries from stdin line by line.
  - Compute and print metrics every 10 lines or upon keyboard interruption (CTRL + C).

### Metrics to Compute

1. **Total File Size**:
   - Compute the sum of the `<file size>` from all processed log entries.
   - Print the total file size in the format: `File size: <total size>`.

2. **Number of Lines by Status Code**:
   - Track the count of each status code: 200, 301, 400, 401, 403, 404, 405, and 500.
   - Print the count for each status code in ascending order.
   - The format should be: `<status code>: <number>`.
   - Ignore any non-integer or unexpected status codes.

### Script Behavior

- The script should print statistics every 10 lines processed.
- On keyboard interruption, the script should print the final statistics before exiting.

### Sample Output

The sample output will look like the following (the actual values will vary):

```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

### Repository Details

- **GitHub Repository**: `alx-interview`
- **Directory**: `0x03-log_parsing`
- **File**: `0-stats.py`

## Usage

1. **Generating Log Data**:
   - Use the provided `0-generator.py` script to generate log data. It simulates log entries and outputs them to stdout.

2. **Running the Log Parsing Script**:
   - Pipe the output from the `0-generator.py` script into `0-stats.py` to process the log entries and display the statistics:
     ```
     ./0-generator.py | ./0-stats.py
     ```

## Conclusion
