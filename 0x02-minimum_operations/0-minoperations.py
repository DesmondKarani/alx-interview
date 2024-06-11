#!/usr/bin/python3
"""
Module 0-minoperations
Contains function minOperations(n) that calculates the fewest
number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in
    exactly n H characters.

    Parameters:
    n (int): The target number of characters.

    Returns:
    int: The minimum number of operations required, or 0 if n is
    impossible to achieve.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n /= factor
        factor += 1

    return operations
