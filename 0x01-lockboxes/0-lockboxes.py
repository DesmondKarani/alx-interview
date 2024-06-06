#!/usr/bin/python3
"""
Module to determine if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): List of boxes where each
        box contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        if current_box not in visited:
            visited.add(current_box)
            for key in boxes[current_box]:
                if key < n:
                    stack.append(key)

    return len(visited) == n


# Example usage and test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Expected: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Expected: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Expected: False
