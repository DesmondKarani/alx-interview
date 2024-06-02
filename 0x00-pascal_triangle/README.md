# Pascal's Triangle in Python

## Overview

This project demonstrates how to generate Pascal's Triangle using Python. Pascal's Triangle is a triangular array of the binomial coefficients, where each number is the sum of the two directly above it. This project includes a Python script that generates Pascal's Triangle for a given number of rows and prints it in a readable format.

## Prerequisites

- Python 3.x

## Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/pascals-triangle.git
    cd pascals-triangle
    ```

2. **Run the Script**:
    ```bash
    python pascals_triangle.py
    ```

3. **Modify the Number of Rows**:
    - Open `pascals_triangle.py`.
    - Change the value of `num_rows` to generate Pascal's Triangle for a different number of rows.
    - Run the script again.

## Functions

### `generate_pascals_triangle(num_rows)`

- **Description**: Generates Pascal's Triangle up to the specified number of rows.
- **Parameters**: `num_rows` (int) - The number of rows of Pascal's Triangle to generate.
- **Returns**: A list of lists representing Pascal's Triangle.

### `print_pascals_triangle(triangle)`

- **Description**: Prints Pascal's Triangle in a readable format.
- **Parameters**: `triangle` (list of lists) - The generated Pascal's Triangle.
- **Returns**: None

## Examples

### Example 1: Generating 5 Rows

```python
num_rows = 5
triangle = generate_pascals_triangle(num_rows)
print_pascals_triangle(triangle)
```

Output:
```
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
```

### Example 2: Generating 7 Rows

```python
num_rows = 7
triangle = generate_pascals_triangle(num_rows)
print_pascals_triangle(triangle)
```

Output:
```
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
```

## Resources

- [What is Pascal’s Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
- [Pascal’s Triangle - Numberphile](https://www.youtube.com/watch?v=XMriWTvPXHI)
- [Python Algorithms](https://www.geeksforgeeks.org/fundamentals-of-algorithms/)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
