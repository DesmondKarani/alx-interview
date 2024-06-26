#!/usr/bin/python3
"""a method that determines if a given data set represents
a valid UTF-8 encoding"""


def validUTF8(data):
    """
    Validate if a given dataset represents a valid UTF-8 encoding.

    Args:
    data (list of int): List of integers representing byte data.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """

    def is_valid_byte(byte):
        return 0 <= byte <= 255

    n_bytes = 0

    for byte in data:
        if not is_valid_byte(byte):
            return False

        binary_repr = format(byte, '08b')

        if n_bytes == 0:
            if binary_repr[0] == '0':
                continue

            leading_ones = 0
            for bit in binary_repr:
                if bit == '1':
                    leading_ones += 1
                else:
                    break

            if leading_ones == 1 or leading_ones > 4:
                return False

            n_bytes = leading_ones - 1

        else:
            if not (binary_repr[0] == '1' and binary_repr[1] == '0'):
                return False
            n_bytes -= 1

    return n_bytes == 0

# Testing the function


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))  # True

    data = [
            80, 121, 116, 104, 111, 110, 32,
            105, 115, 32, 99, 111, 111, 108, 33
            ]
    print(validUTF8(data))  # True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # False
