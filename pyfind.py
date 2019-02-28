#!/usr/bin/env python
import sys
import re

# cmd line:   pyfind.py PATTERN FILE ....
rx_pattern = re.compile(sys.argv[1])     # pattern
file_list = sys.argv[2:]  # files

for file_name in file_list:
    with open(file_name) as file_in:
        for i, line in enumerate(file_in, 1):
            if rx_pattern.search(line):
                print(f"{i:6d} {line.rstrip()}")
    print("====")
