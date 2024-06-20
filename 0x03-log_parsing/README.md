# 0x03. Log Parsing

## Overview

This project involves creating a Python program that reads log data from standard input (stdin) in real-time, processes the data to extract specific information, and computes metrics based on the processed data. The program needs to handle various input formats, manage interruptions gracefully, and ensure data integrity throughout its execution.

## Concepts Covered

1. **File I/O in Python**:
   - Reading from `sys.stdin` line by line.
   - Relevant resource: [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

2. **Signal Handling in Python**:
   - Handling keyboard interruptions (CTRL + C) using signal handling.
   - Relevant resource: [Python Signal Handling](https://docs.python.org/3/library/signal.html)

3. **Data Processing**:
   - Parsing strings to extract specific data points.
   - Aggregating data to compute summaries.

4. **Regular Expressions**:
   - Using regular expressions to validate the format of each line.
   - Relevant resource: [Python Regular Expressions](https://docs.python.org/3/library/re.html)

5. **Dictionaries in Python**:
   - Using dictionaries to count occurrences of status codes and accumulate file sizes.
   - Relevant resource: [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

6. **Exception Handling**:
   - Handling possible exceptions that may arise during file reading and data processing.
   - Relevant resource: [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)

## Requirements

- **Editors**: vi, vim, emacs
- **Interpreter/Compiler**: Ubuntu 20.04 LTS using python3 (version 3.4.3)
- **File Specifications**:
  - All files should end with a new line.
  - The first line of all files should be exactly `#!/usr/bin/python3`.
  - Code must adhere to PEP 8 style (version 1.7.x).
  - All files must be executable.
  - File lengths will be tested using `wc`.

## Project Structure

The root folder of the project must contain:
- `README.md` (this file)
- Python scripts implementing the log parsing functionality

## Getting Started

1. **Clone the repository**:
   ```sh
   git clone <repository-url>
   ```

2. **Navigate to the project directory**:
   ```sh
   cd 0x03-log_parsing
   ```

3. **Run the program**:
   ```sh
   ./your_script.py
   ```

4. **Provide input**:
   - The program reads from stdin, so you can pipe data into it or run it and type input directly.

## Example Usage

```sh
$ echo "Sample log data" | ./your_script.py
```

## Additional Resources

- [Mock Technical Interview](https://www.example.com/mock-interview)

By studying the above concepts and following the guidelines, you will be able to successfully complete the log parsing project, ensuring your program can handle data streams, parse log entries, and compute necessary metrics efficiently and accurately.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
