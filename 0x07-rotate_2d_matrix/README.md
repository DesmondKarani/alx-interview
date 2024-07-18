# 0x07. Rotate 2D Matrix

## Description
This project contains a Python implementation of an algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. The rotation is performed in-place, meaning the original matrix is modified without creating a new matrix.

## Project Info
- **Language**: Python
- **Project Type**: Algorithm
- **Weight**: 1

## Project Schedule
- **Start Date**: Jul 15, 2024 6:00 AM
- **End Date**: Jul 19, 2024 6:00 AM
- **Checker Release**: Jul 16, 2024 6:00 AM
- **Auto Review**: Will be launched at the deadline

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.10)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.8.0)
- You are not allowed to import any module
- All modules and functions must be documented
- All your files must be executable

## Task: Rotate 2D Matrix
### Prototype
```python
def rotate_2d_matrix(matrix):
```

### Description
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

- Do not return anything. The matrix must be edited in-place.
- You can assume the matrix will have 2 dimensions and will not be empty.

### Example
```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)
```

Output:
```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Usage
1. Ensure you have Python 3.8.10 installed on your system.
2. Clone this repository: `git clone [repository-url]`
3. Navigate to the project directory: `cd 0x07-rotate_2d_matrix`
4. Run the main script: `./0-main.py`

## File Description
- `0-rotate_2d_matrix.py`: Contains the implementation of the `rotate_2d_matrix` function.
- `0-main.py`: A sample main file to test the `rotate_2d_matrix` function.

## Author
[Your Name]

## License
This project is licensed under the terms of the MIT license.
