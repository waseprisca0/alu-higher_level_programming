#!/usr/bin/python3
import sys
from collections import defaultdict

TOTAL_SIZE = 0
STATUS_CODES = defaultdict(int)
LINE_COUNT = 0

try:
    for line in sys.stdin:
        LINE_COUNT += 1
        parts = line.strip().split()
        if len(parts) == 5:
            ip_address, _, _, status_code, file_size = parts
            TOTAL_SIZE += int(file_size)
            STATUS_CODES[status_code] += 1

        if LINE_COUNT % 10 == 0:
            print(f"Total file size: {TOTAL_SIZE}")
            for status_code in sorted(STATUS_CODES.keys()):
                print(f"{status_code}: {STATUS_CODES[status_code]}")
            print()

except KeyboardInterrupt:
    print(f"\nTotal file size: {TOTAL_SIZE}")
    for status_code in sorted(STATUS_CODES.keys()):
        print(f"{status_code}: {STATUS_CODES[status_code]}")
