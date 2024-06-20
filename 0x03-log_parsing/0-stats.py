#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""

import sys
import signal

total_size = 0
status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }
line_count = 0


def print_stats():
    """ Print the accumulated statistics """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """ Handle the interrupt signal (CTRL + C) """
    print_stats()
    sys.exit(0)


# Set up the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Ensure the line matches the expected format
        if len(parts) < 7:
            continue

        ip, dash, date, method, path, protocol, status_code, file_size = (
                parts[0], parts[1], parts[2], parts[3],
                parts[4], parts[5], parts[6], parts[7]
                )

        # Validate status code and file size
        if (
                status_code.isdigit() and
                status_code in status_codes and
                file_size.isdigit()
                ):
            status_codes[status_code] += 1
            total_size += int(file_size)

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

print_stats()
