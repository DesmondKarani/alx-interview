# 0x08. Making Change

## Algorithm
## Python

### Project Description
This project tackles the classic coin change problem, which is a fundamental problem in the domain of dynamic programming and greedy algorithms. The goal is to determine the minimum number of coins needed to make up a given total amount, given a list of coin denominations.

### Task
0. Change comes from within
   - File: `0-making_change.py`
   - Prototype: `def makeChange(coins, total)`
   - Return: Fewest number of coins needed to meet total
   - If total is 0 or less, return 0
   - If total cannot be met by any number of coins you have, return -1
   - `coins` is a list of the values of the coins in your possession
   - The value of a coin will always be an integer greater than 0
   - You can assume you have an infinite number of each denomination of coin in the list

### Requirements
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable

### Evaluation
Your solution's runtime will be evaluated in this task.

### Example
```python
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
