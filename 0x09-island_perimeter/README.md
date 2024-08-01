# 0x09. Island Perimeter

## Description
This project involves creating a function that calculates the perimeter of an island in a grid. The grid is represented by a 2D list where 0 represents water and 1 represents land.

## Task
### 0. Island Perimeter
Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:

- `grid` is a list of list of integers:
  - 0 represents water
  - 1 represents land
- Each cell is square, with a side length of 1
- Cells are connected horizontally/vertically (not diagonally)
- The grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing)
- The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island)

## Requirements
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use the PEP 8 style (version 1.7)
- You are not allowed to import any module
- All modules and functions must be documented
- All files must be executable
